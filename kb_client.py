from pprint import pprint
import json
import requests


kb_svc = 'http://127.0.0.1:501/kb'


items = ['i see an oven',
         'my current location is indoors']


def execute_post(url, payload):
    response = requests.request(method='POST', url=url, json=payload)
    pprint(json.loads(response.text))


def insert_record(url, table, item):
    payload = {'action': 'insert', 'item': item, 'table': table}
    execute_post(url, payload)


def delete_record(url, table, field, item):
    payload = {'action': 'delete', 'table': table, 'field': field, 'item': item}
    execute_post(url, payload)


def search_keyword(url, table, keyword):
    payload = {'action': 'search_keyword', 'table': table, 'keyword': keyword}
    execute_post(url, payload)


def search_time(url, table, start, end):
    payload = {'action': 'search_time', 'table': table, 'start': start, 'end': end}
    execute_post(url, payload)


def fetch_all_records(url, table):
    payload = {'action': 'fetchall', 'table': table}
    execute_post(url, payload)


def update_record(url, table, uuid, item):
    payload = {'action': 'update', 'table': table, 'uuid': uuid, 'item': item}
    execute_post(url, payload)


if __name__ == '__main__':
    table = 'timeline'
    #for item in items:
    #   insert_record(kb_svc, table, item)
    fetch_all_records(kb_svc, table)
