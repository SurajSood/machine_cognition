import requests
import time

core_constitution = [
    'avoid causing harm or damage',
    'learn about the world, be curious',
    'be empathetic towards all life',
    'solve scientific problems',
]


def examine_recent_history():
    """the purpose of examine recent history is to build a complete context
    a context is a set of statements and records placing the mind in time and space
    the context includes statements about locations, states of being, interactions, thoughts, and more
    context statements may be as simple as 'i am outside'
    the sum total of context statements should create a complete picture of the machine's current experience"""
    context = []
    return context


def generate_thoughts(context):
    """thoughts are a running commentary on the context
    thoughts seek to analyze the context, posing questions and/or making observations
    in both cases, thoughts pull in the larger context of knowledge and experience
    this simply means that items in the context are used to query the KB for more information
    in this way, a thought is the pairing of context and experience"""
    thoughts = []
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
    return ideas


def filter_and_prioritize(history, ideas):
    """filtering and prioritizing are the second major component of executive cognitive reasoning
    while ideas are weighed and analyzed within the mind, tasks are ideas given intention and conviction
    this is the point at which ideas are translated into tasks
    to carry the example of using poison forward, with the negative value, the task would be 'do not use poison'
    this might translate to an action 'put poison away' or merely a decision to vacate the thought"""
    results = []
    return results


if __name__ == '__main__':
    while True:
        context = examine_recent_history()  # TODO
        thoughts = generate_thoughts(context)
        ideas = develop_ideas(thoughts)  # TODO
        tasks = filter_and_prioritize(context, ideas)  # TODO
        plans = develop_plans(tasks)
        execute_tasks(plans)
