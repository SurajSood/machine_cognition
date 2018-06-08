import json
import requests


if __name__ == '__main__':
    payload = {'identity': 'dave', 'sentence': 'hello, how are you?'}
    #response = requests.request(method='PUT', url='http://127.0.0.1:500/convo', json=payload)
    #print(response, response.text)
    response = requests.request(method='GET', url='http://127.0.0.1:500/convo')
    conversation = json.loads(response.text)
    for i in conversation:
        print(i)