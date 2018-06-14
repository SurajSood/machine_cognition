import random

sys = random.SystemRandom()


def random_statement():
    subj = ['kitchen', 'bacon', 'history', 'automobile', 'I']
    sob = ['is', 'is not', 'will be', 'cannot be', 'contains', 'is made of', 'is part of', 'am not']
    state = ['blue', 'heavy', 'kitchen sink', 'a house', 'stupid', 'green', 'alive']
    w1 = sys.choice(subj)
    w2 = sys.choice(sob)
    w3 = sys.choice(state)
    print(w1, w2, w3)


def random_question():
    qwords = ['how', 'who', 'what', 'where', 'when', 'why']
    sob = ['is', 'is not', 'will be', 'cannot be', 'contains', 'is made of', 'is part of', 'am']
    thing = ['time', 'car', 'you', 'me']
    w1 = sys.choice(qwords)
    w2 = sys.choice(sob)
    w3 = sys.choice(thing)
    print(w1, w2, w3)


def random_action():
    self = ['i will', 'i will not', 'i cannot', 'i want to', 'i do not want to']
    verb = ['travel to', 'clean', 'remember', 'lift', 'break', 'stab']
    subject = ['the kitchen', 'the basement', 'the sky', 'the person', 'the house', 'the cat', 'the dog', 'the road']
    w1 = sys.choice(self)
    w2 = sys.choice(verb)
    w3 = sys.choice(subject)
    print(w1, w2, w3)


if __name__ == '__main__':
    while True:
        random_question()
        random_statement()
        random_action()
