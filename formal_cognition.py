from pprint import pprint
import requests
import time
import json

kb_svc = 'http://127.0.0.1:501/kb'
nlp_svc = 'http://127.0.0.1:501/nlp'


def execute_post(url, payload):
    response = requests.request(method='POST', url=url, json=payload)
    return json.loads(response.text)


def examine_recent_history():
    """the purpose of examine recent history is to build a complete context
    a context is a set of statements and records placing the mind in time and space
    the context includes statements about locations, states of being, interactions, thoughts, and more
    context statements may be as simple as 'i am outside'
    the sum total of context statements should create a complete picture of the machine's current experience"""
    context = []
    # ex: 'david said go to the kitchen'
    tables = ['chronology', 'stream']
    for table in tables:
        payload = {'action': 'search_time', 'table': table, 'start': str(time.time()-3600), 'end': str(time.time())}
        data = execute_post(kb_svc, payload)
        context.append(data)
    return context


def generate_thoughts(context):
    """thoughts are a running commentary on the context
    thoughts seek to analyze the context, posing questions and/or making observations
    in both cases, thoughts pull in the larger context of knowledge and experience
    this simply means that items in the context are used to query the KB for more information
    in this way, a thought is the pairing of context and experience"""
    thoughts = []
    for item in context:
        payload = {'action': 'get_keywords', 'item': item['item']}
        keywords = execute_post(nlp_svc, payload)
        payload = {'action': 'generate_permutations', 'item': item['item']}
        permutations = execute_post(nlp_svc, payload)
        # need to filter out gibberish permutations at this point
        # nlp_word_salad
        for keyword in keywords:
            payload = {'action': 'search_keyword', 'table': 'world', 'keyword': keyword}
            thoughts.append(execute_post(kb_svc, payload))
            payload = {'action': 'search_keyword', 'table': 'people', 'keyword': keyword}
            thoughts.append(execute_post(kb_svc, payload))
            payload = {'action': 'search_keyword', 'table': 'identity', 'keyword': keyword}
            thoughts.append(execute_post(kb_svc, payload))
    # ex. 'i should go to the kitchen'
    return thoughts


def develop_ideas(thoughts):
    """an idea is a formal thought
    thoughts are casual and abstract, and may be completely meaningless
    ideas are thoughts taken out to logical conclusions
    whereby the validity or impact of a thought can be measured
    for instance, if a thought of interacting with poison comes to mind
    one logical result (prognosis) could be causing harm or death
    this would violate the core constitution and thus be rated as having negative value"""
    ideas = []
    for item in thoughts:
        corpus = compile_corpus(item)  # TODO
        prognosis = anticipate_results(corpus)  # TODO
        value = evaluate_prognosis(corpus, prognosis)  # TODO
        ideas.append({'corpus': corpus, 'prognosis': prognosis, 'value': value})
    # ex: corpus: 'i will travel to/find/search for the kitchen; a kitchen is a place for cooking food... etc
    # ex: prognosis: 'i will be located in a kitchen; i will see an oven and a microwave'
    # ex: value: 'high; aligns with identity values'
    return ideas


def filter_and_prioritize(context, ideas):
    """filtering and prioritizing are the second major component of executive cognitive reasoning
    while ideas are weighed and analyzed within the mind, tasks are ideas given intention and conviction
    this is the point at which ideas are translated into tasks
    to carry the example of using poison forward, with the negative value, the task would be 'do not use poison'
    this might translate to an action 'put poison away' or merely a decision to vacate the thought
    the personal identity table is the primary source for filtration and prioritization"""
    results = []
    # filtered list of ideas
    return results


def develop_plans(tasks):
    """developing plans is where the ideas are matched with actual services and workflows available to the machine
    as part of this processes, the necessary information is compiled for each service
    for instance, a navigation or search service may need a direction, destination, or search goal
    generally speaking, the necessary information should have been added when the corpus was compiled
    however it may also take more NLP to parse out the specific objective from the corpus
    a plan is simply a dictionary that contains the service as well as input variables for the service"""
    plans = []
    # ex: task service: travel_search
    # ex: search criteria: oven, microwave, pantry, food, cookware
    # ex: success condition: criteria > %60
    return plans


if __name__ == '__main__':
    while True:
        context = examine_recent_history()  # TODO
        pprint(context)
        exit()
        thoughts = generate_thoughts(context)  # TODO
        ideas = develop_ideas(thoughts)  # TODO
        tasks = filter_and_prioritize(context, ideas)  # TODO
        plans = develop_plans(tasks)  # TODO
        execute_tasks(plans)  # TODO
