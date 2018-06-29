from pprint import pprint
import nltk
from nltk.corpus import wordnet


def compile_action_concept(verb):
    results = []
    syns = wordnet.synsets(verb)
    for x in syns:
        if x.pos() != 'v':
            continue
        else:
            results.append(x.definition())
    return results


def compile_subject_concept(noun):
    results = [noun]
    syns = wordnet.synsets(noun)
    for x in syns:
        if x.pos() != 'n':
            continue
        else:
            results.append(x.definition())
            hypers = x.hypernyms()
            for h in hypers:
                results.append(h.definition())
    return results


if __name__ == '__main__':
    #s = 'go to the kitchen'
    s = 'remember to clean the floor'
    t = nltk.word_tokenize(s)
    p = nltk.pos_tag(t)
    for i in p:
        if i[1] == 'NN':
            concept = compile_subject_concept(i[0])
            pprint(concept)
        elif 'V' in i[1]:
            concept = compile_action_concept(i[0])
            pprint(concept)