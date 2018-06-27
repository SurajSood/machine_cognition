import time
import sqlite3
import json
from pprint import pprint
import nltk
import flask
from nltk.corpus import wordnet


database = sqlite3.connect('chatbot.sqlite')
cursor = database.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS chatbot (time, entity, message);')
database.commit()


def save_message(entity, message):
    values = (time.time(), entity, message)
    cursor.execute('INSERT INTO chatbot (time, entity, message) VALUES (?, ?, ?);', values)
    database.commit()


def compose_response():



app = flask.Flask(__name__)


@app.route('/chat', methods=['POST'])
def default():
    request = flask.request
    data = json.loads(request.data)
    print(data)  # data should be {'message': 'blah blah blah', 'entity': 'dave'}
    save_message(data['entity'], data['message'])
    convo_state = predict_convo_state()




if __name__ == '__main__':
    # need to simplify like kb service
    app.run(port=502)
