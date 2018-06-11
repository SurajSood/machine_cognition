import uuid
import time
import sqlite3
import json
import flask


connection = sqlite3.connect('kb.db')
cursor = connection.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS identity (uuid, time, item);')
cursor.execute('CREATE TABLE IF NOT EXISTS chronology (uuid, time, item);')  # conversation goes into chronology, for ex
cursor.execute('CREATE TABLE IF NOT EXISTS people (uuid, time, item);')
cursor.execute('CREATE TABLE IF NOT EXISTS world (uuid, time, item);')
cursor.execute('CREATE TABLE IF NOT EXISTS stream (uuid, time, item);')
connection.commit()


app = flask.Flask(__name__)


@app.route('/kb', methods=['POST'])
def default():
    request = flask.request
    payload = json.loads(request.data)
    print('INCOMING PAYLOAD', payload)

    if payload['action'] == 'insert':
        values = (str(uuid.uuid4()), str(time.time()), str(payload['item']))
        cursor.execute('INSERT INTO %s (uuid, time, item) VALUES (?, ?, ?);' % payload['table'], values)
        connection.commit()
        print('ADDED TO', payload['table'], values)
        return json.dumps({'result': 'success', 'values': values})

    elif payload['action'] == 'fetchall':
        results = cursor.execute('SELECT * FROM %s;' % payload['table']).fetchall()
        output = [{'uuid': i[0], 'time': i[1], 'item': i[2]} for i in results]
        print('DUMPING ALL FROM', payload['table'])
        return json.dumps(output)

    elif payload['action'] == 'delete':
        delete = (payload['table'], payload['field'], payload['item'])
        cursor.execute('DELETE FROM %s WHERE %s="%s";' % delete)
        connection.commit()
        print('DELETION FROM', delete)
        return json.dumps({'result': 'success', 'action': delete})

    elif payload['action'] == 'search':
        results = cursor.execute('SELECT * FROM %s WHERE %s LIKE ' % (payload['table'], payload['field']) + '"%' + payload['keyword'] + '%";')
        payload = [{'uuid': i[0], 'time': i[1], 'item': i[2]} for i in results]
        print('dumping search results')
        return json.dumps(payload)


if __name__ == '__main__':
    app.run(port=501)
