from pprint import pprint
import json
import requests


core_constitution = [
    'i will avoid causing harm or damage',
    'i will learn about the world',
    'i will be empathetic towards all life',
    'i want to help solve scientific problems'
]


if __name__ == '__main__':
    for c in core_constitution:
        response = requests.request(method='PUT', url='http://127.0.0.1:501/identity', json=c)
        print(json.loads(response.text))
    response = requests.request(method='GET', url='http://127.0.0.1:501/identity')
    for i in json.loads(response.text):
        print(i['fact'])