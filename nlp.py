import json
from pprint import pprint
import nltk
import flask
from nltk.corpus import wordnet


def dialogue_act_features(post):
    features = {}
    for word in nltk.word_tokenize(post):
        features['contains({})'.format(word.lower())] = True
    return features


def dialogue_act_model():
    posts = nltk.corpus.nps_chat.xml_posts()[:10000]
    featuresets = [(dialogue_act_features(post.text), post.get('class')) for post in posts]
    size = int(len(featuresets) * 0.1)
    train_set, test_set = featuresets[size:], featuresets[:size]
    classifier = nltk.NaiveBayesClassifier.train(train_set)
    print(nltk.classify.accuracy(classifier, test_set))
    return classifier


def get_all_syns(word):
    result = []
    for synset in wordnet.synsets(word):
        print('DEFINITION', synset.definition())
        for lemma in synset.lemmas():
            result.append(lemma.name())
    return result


def get_all_meanings(word):
    result = []
    for synset in wordnet.synsets(word):
        result.append(synset.definition())
    return result


def sentence_permutations(sentence):
    result = []
    for word in nltk.tokenize.word_tokenize(sentence):
        meanings = get_all_meanings(word)
        result.append(meanings or [word])
    return result


dialogue_model = dialogue_act_model()
app = flask.Flask(__name__)


@app.route('/permutations', methods=['POST'])
def default():
    request = flask.request
    data = json.loads(request.data)
    print(data)
    permutations = sentence_permutations(data)
    return json.dumps(permutations)


@app.route('/dialogue', methods=['POST'])
def default():
    request = flask.request
    data = json.loads(request.data)
    print(data)
    fset = dialogue_act_features(data)
    act = dialogue_model.classify(fset)
    return json.dumps(act)


if __name__ == '__main__':
    # need to simplify like kb service
    app.run(port=502)
