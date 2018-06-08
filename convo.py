import time
import sqlite3
import json
import flask


connection = sqlite3.connect('convo.db')
cursor = connection.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS conversation (time, identity, sentence);')
connection.commit()


def inbound_communication(identity, sentence):
    values = (time.time(), identity, sentence)
    cursor.execute('INSERT INTO conversation (time, identity, sentence) VALUES (?, ?, ?);', values)
    connection.commit()


app = flask.Flask(__name__)


@app.route('/convo', methods=['PUT', 'GET', 'POST'])
def default():
    request = flask.request
    if request.method == 'PUT':
        request = json.loads(request.data)  # expect identity, sentence
        print(request)
        inbound_communication(request['identity'], request['sentence'])
        return json.dumps({'result': 'sentence recorded'})
    elif request.method == 'GET':
        results = cursor.execute('SELECT * FROM conversation;').fetchall()
        payload = [{'time': i[0], 'identity': i[1], 'sentence': i[2]} for i in results]
        print('dumping entire conversation')
        return json.dumps(payload)


if __name__ == '__main__':
    app.run(port=500)