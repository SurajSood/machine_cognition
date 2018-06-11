from pprint import pprint
import json
import requests


kb_svc = 'http://127.0.0.1:501/kb'


def insert_record(url, table, item):
    payload = {'action': 'insert', 'item': item, 'table': table}
    response = requests.request(method='POST', url=url, json=payload)
    print(json.loads(response.text))


def delete_record(url, table, field, item):
    payload = {'action': 'delete', 'table': table, 'field': field, 'item': item}
    response = requests.request(method='POST', url=url, json=payload)
    print(json.loads(response.text))


def search_record(url, table, field, keyword):
    payload = {'action': 'search', 'table': table, 'field': field, 'keyword': keyword}
    response = requests.request(method='POST', url=url, json=payload)
    pprint(json.loads(response.text))


def fetch_all_records(url, table):
    payload = {'action': 'fetchall', 'table': table}
    response = requests.request(method='POST', url=url, json=payload)
    pprint(json.loads(response.text))


if __name__ == '__main__':
    fetch_all_records(kb_svc, 'identity')
