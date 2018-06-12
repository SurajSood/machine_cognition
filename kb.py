import uuid
import time
import sqlite3
import json
import flask


connection = sqlite3.connect('kb.db')
cursor = connection.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS identity (uuid, time, item);')
cursor.execute('CREATE TABLE IF NOT EXISTS timeline (uuid, time, item);')
cursor.execute('CREATE TABLE IF NOT EXISTS knowledge (uuid, time, item);')
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
        return json.dumps({'result': 'success', 'values': values})

    elif payload['action'] == 'delete':
        values = (payload['table'], payload['uuid'])
        cursor.execute('DELETE FROM %s WHERE uuid="%s";' % values)
        connection.commit()
        return json.dumps({'result': 'success', 'action': values})

    elif payload['action'] == 'search_keyword':
        values = (payload['table'], payload['keyword'])
        results = cursor.execute('SELECT * FROM %s WHERE item LIKE "%%%s%%";' % values)
        return json.dumps([{'uuid': i[0], 'time': i[1], 'item': i[2]} for i in results])

    elif payload['action'] == 'search_time':
        values = (payload['table'], payload['start'], payload['end'])
        results = cursor.execute('SELECT * FROM %s WHERE time > "%s" AND time < "%s";' % values)
        return json.dumps([{'uuid': i[0], 'time': i[1], 'item': i[2]} for i in results])

    elif payload['action'] == 'fetchall':
        results = cursor.execute('SELECT * FROM %s;' % payload['table']).fetchall()
        return json.dumps([{'uuid': i[0], 'time': i[1], 'item': i[2]} for i in results])


if __name__ == '__main__':
    app.run(port=501)
