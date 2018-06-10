import requests
import time

top_level_imperatives = [
    'avoid causing harm or damage',
    'learn about the world, be curious',
    'be empathetic towards all life',
]


def examine_recent_history():
    # query chronology and stream of consciousness
    results = []
    return results


def expound_candidate(cand):
    # enumerate possibilities TODO
    results = []
    return results


def identify_tasks_or_directives(history):
    candidates = []
    for item in history:
        candidates.append(expound_candidate(item))
    results = []
    for item in candidates:
        corpus = compile_corpus(item)  # TODO
        prognosis = anticipate_results(corpus)  # TODO
        value = evaluate_task_results(corpus, prognosis)  # TODO
        results.append({'corpus': corpus, 'prognosis': prognosis, 'value': value})
    return results


def filter_and_prioritize(history, tasks):
    # weigh tasks and prognoses against imperatives
    # generate relativistic score for each imperative against each task
    # sort and filter
    results = []
    return results


def execute_tasks(tasks):
    # record decisions in stream of consciousness
    # for each task, clarify actions and goals (summarize, simplify, etc)
    # initiate tasks via REST, or take no action to let existing tasks complete
    # note: tasks will update the kb service
    print('bacon')


if __name__ == '__main__':
    my_current_state = top_level_imperatives[0]
    while True:
        history = examine_recent_history()  # TODO
        tasks = identify_tasks_or_directives(history)  # TODO
        tasks = filter_and_prioritize(history, tasks)  # TODO
        execute_tasks(tasks)  # TODO
        time.sleep(30)
