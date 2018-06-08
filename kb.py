import uuid
import time
import sqlite3
import json
import flask


connection = sqlite3.connect('kb.db')
cursor = connection.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS identity (uuid, fact);')
cursor.execute('CREATE TABLE IF NOT EXISTS chronology (time, event);')
cursor.execute('CREATE TABLE IF NOT EXISTS people (uuid, person, fact);')
cursor.execute('CREATE TABLE IF NOT EXISTS world (uuid, fact);')
connection.commit()


app = flask.Flask(__name__)


@app.route('/identity', methods=['PUT', 'GET'])
def default():
    request = flask.request
    if request.method == 'PUT':
        request = json.loads(request.data)
        uid = uuid.uuid4()
        values = (uid, request['fact'])
        cursor.execute('INSERT INTO identity (uuid, fact) VALUES (?, ?);', values)
        connection.commit()
        print('ADDED FACT', values)
        return uid
    elif request.method == 'GET':
        results = cursor.execute('SELECT * FROM identity;').fetchall()
        payload = [{'uuid': i[0], 'fact': i[1]} for i in results]
        print('dumping personal identity')
        return json.dumps(payload)


@app.route('/chronology', methods=['PUT', 'GET'])
def default():
    request = flask.request
    if request.method == 'PUT':
        request = json.loads(request.data)
        t = time.time()
        values = (t, request['event'])
        cursor.execute('INSERT INTO chronology (time, event) VALUES (?, ?);', values)
        connection.commit()
        print('ADDED EVENT', values)
        return t
    elif request.method == 'GET':
        results = cursor.execute('SELECT * FROM chronology;').fetchall()
        payload = [{'time': i[0], 'event': i[1]} for i in results]
        print('dumping personal chronology')
        return json.dumps(payload)


@app.route('/people', methods=['PUT', 'GET'])
def default():
    request = flask.request
    if request.method == 'PUT':
        request = json.loads(request.data)
        uid = uuid.uuid4()
        values = (uid, request['person'], request['fact'])
        cursor.execute('INSERT INTO people (uuid, person, fact) VALUES (?, ?, ?);', values)
        connection.commit()
        print('ADDED FACT', values)
        return uid
    elif request.method == 'GET':
        results = cursor.execute('SELECT * FROM people;').fetchall()
        payload = [{'uuid': i[0], 'person': i[1], 'fact': i[2]} for i in results]
        print('dumping people database')
        return json.dumps(payload)


@app.route('/world', methods=['PUT', 'GET', 'POST', 'DELETE'])
def default():
    request = flask.request
    if request.method == 'PUT':
        request = json.loads(request.data)
        uid = uuid.uuid4()
        values = (uid, request['fact'])
        cursor.execute('INSERT INTO world (uuid, fact) VALUES (?, ?);', values)
        connection.commit()
        print('ADDED FACT', values)
        return uid
    elif request.method == 'GET':
        results = cursor.execute('SELECT * FROM world;').fetchall()
        payload = [{'uuid': i[0], 'fact': i[1]} for i in results]
        print('dumping world knowledge')
        return json.dumps(payload)
    elif request.method == 'POST':
        request = json.loads(request.data)
        results = cursor.execute('SELECT * FROM world WHERE uuid="%s";' % request['uuid']).fetchall()
        payload = [{'uuid': i[0], 'fact': i[1]} for i in results]
        print('returning world knowledge query')
        return json.dumps(payload)
    elif request.method == 'DELETE':
        request = json.loads(request.data)
        results = cursor.execute('SELECT * FROM world WHERE uuid="%s";' % request['uuid']).fetchall()
        payload = [{'uuid': i[0], 'fact': i[1]} for i in results]
        cursor.execute('DELETE FROM world WHERE uuid="%s";' % request['uuid'])
        print('deleting precious knowledge', payload)
        return json.dumps(payload)


if __name__ == '__main__':
    app.run(port=501)
