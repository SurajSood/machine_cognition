import random
import time
import requests


kb_svc = 501
kb_apis = ['identity', 'people', 'world', 'chronology', 'stream']


if __name__ == '__main__':
    while True:
        for api in kb_apis:
            random.seed()
            idea = get_random_idea(api)
            ponder = bool(random.getrandbits(1))
            if ponder:
                idea = ponder_idea(idea)
            deposit_idea(idea)
        time.sleep(20)