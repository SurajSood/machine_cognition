import nltk
from nltk.corpus import wordnet


def find_distance(w1, w2):
    word1 = wordnet.synset(w1)
    word2 = wordnet.synset(w2)
    print(word1, word2)
    taxonomy_distance = word1.shortest_path_distance(word2)
    wup = word1.wup_similarity(word2)
    print(taxonomy_distance, wup)
    print('\r\n')


def antonym_distance(w1, w2):
    word1 = wordnet.synset(w1)
    word2 = wordnet.synset(w2)
    w2lemmas = word2.lemmas()
    for l in word1.lemmas():
        for ant in l.antonyms():
            if ant in w2lemmas:
                return True
    return False


if __name__ == '__main__':
    #find_distance('house.n.01', 'structure.n.01')
    #find_distance('always.r.01', 'never.r.01')
    #find_distance('run.v.01', 'quick.a.01')
    t = antonym_distance('always.r.01', 'never.r.01')
    print(t)
    t = antonym_distance('blue.a.01', 'red.a.01')
    print(t)
    t = antonym_distance('go.v.01', 'stop.v.01')
    print(t)
