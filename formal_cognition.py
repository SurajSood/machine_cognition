from pprint import pprint
import requests
import time
import json

kb_svc = 'http://127.0.0.1:501/kb'
nlp_svc = 'http://127.0.0.1:501/nlp'


def execute_post(url, payload):
    response = requests.request(method='POST', url=url, json=payload)
    return json.loads(response.text)


def generate_particles(timeline):
    """
    particles are 'thoughts' and 'ideas' based upon recent input and states of being
    """
    particles = []
    for event in timeline:
        print(event)
    return particles


def filter_particles(particles, identity):
    """
    particles that are gibberish will be removed
    particles that violate personal identity will be removed
    """
    return particles


def prioritize_particles(particles, identity):
    """
    particles will be scored based upon adherence to personal identity
    particle scores will be weighted based upon recency
    """
    return particles


def commit_particles(particles):
    """
    particles will be committed to the timeline
    """
    for p in particles:
        requests.request(p)


def fetch_all(url, table):
    payload = {'action': 'fetchall', 'table': table}
    return execute_post(url, payload)


if __name__ == '__main__':
    while True:
        identity = fetch_all(kb_svc, 'identity')
        timeline = fetch_all(kb_svc, 'timeline')
        particles = generate_particles(timeline)
        particles = filter_particles(particles, identity)
        particles = prioritize_particles(particles, identity)
        commit_particles(particles)
        time.sleep(2)
