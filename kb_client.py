from pprint import pprint
import json
import requests


core_constitution = [
]


if __name__ == '__main__':
    #for c in core_constitution:
        #response = requests.request(method='PUT', url='http://127.0.0.1:501/identity', json=c)
        #print(json.loads(response.text))
    response = requests.request(method='GET', url='http://127.0.0.1:501/identity')
    pprint(json.loads(response.text))