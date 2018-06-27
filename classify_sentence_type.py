import numpy as np
from sklearn.svm import SVC
import re
import random


"""
classes
    interrogative (questions)
    imperative (orders, commands)
    declarative (facts, statements)
    exclamatory (invective, surprise, emphasis)

imperative sentences
    http://englishsentences.com/imperative-sentence/
    http://examples.yourdictionary.com/imperative-sentence-examples.html
    https://www.examples.com/education/imperative-sentence-examples.html
    https://literarydevices.net/imperative-sentence/

declarative sentences
    https://english.stackexchange.com/questions/113423/imperative-vs-declarative-can-a-third-grader-or-his-parents-tell-the-differenc
    https://study.com/academy/lesson/comparing-declarative-imperative-sentences.html
    https://study.com/academy/lesson/declarative-sentence-definition-examples.html
    http://www.englishlanguageguide.com/grammar/declarative-sentence.asp
    https://www.english-grammar-revolution.com/declarative-sentence.html
    http://englishsentences.com/declarative-sentence/
    
"""


if __name__ == '__main__':
    with open('novels/hound_baskervilles_conan_doyle.txt', encoding='utf8') as infile:
        novel = infile.read()
    novel = novel.replace('\n', ' ')
    #print(novel)
    regex = re.compile(r',”.*?“')
    novel = regex.sub(' ', novel)
    novel = novel.replace('-', ' ')
    dialog = re.findall(r'“.*?”', novel)
    questions = []
    for i in dialog:
        i = i.replace('”', '').replace('“', '').replace('  ', ' ')
        i = i.replace('? ', '?\n').replace('  ', ' ')
        i = i.splitlines()
        i = [q.strip() for q in i]
        questions += i
    exclamations = []
    for i in questions:
        i = i.replace('! ', '!\n').replace('  ', ' ')
        i = i.splitlines()
        i = [q.strip() for q in i]
        exclamations += i
    periods = []
    for i in exclamations:
        i = i.replace('Mrs.', 'Mrs').replace('Mr.', 'Mr').replace('Dr.', 'Dr').replace('. ', '.\n').replace('  ', ' ')
        i = i.splitlines()
        i = [q.strip() for q in i]
        periods += i

    for i in periods:
        print(i)
    exit()
    word_list = []
    for i in periods:
        i = i.lower()
        words = re.findall(r'\w+', i)
        for w in words:
            if w not in word_list:
                word_list.append(w)
    print(word_list)
    print(len(word_list))

    data = []
    for i in periods:
        i = i.lower()
        if i.endswith('?'):
            label = 'question'
        else:
            label = 'statement'
        words = re.findall(r'\w+', i)
        sample = [0] * len(word_list)
        for word in words:
            idx = word_list.index(word)
            sample[idx] += 1
        data.append((sample, label))
    sys = random.SystemRandom()
    sys.shuffle(data)
    half = int(len(data) / 2)
    training = data[:half]
    test = data[half:]
