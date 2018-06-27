import numpy as np
from scipy.stats import linregress
import nltk
from sklearn.svm import SVC


pos_index = ['CC', 'CD', 'DT', 'EX', 'FW', 'IN', 'JJ', 'JJR', 'JJS', 'LS', 'MD', 'NN', 'NNP', 'NNPS', 'NNS', 'PDT', 'POS', 'PRP', 'PRP$', 'RB', 'RBR', 'RBS', 'RP', 'SYM', 'TO', 'UH', 'VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ', 'WDT', 'WP', 'WP$', 'WRB']


train = [('i am a banana', 'declarative'),
         ('what are you doing', 'interrogative'),
         ('the weather sure is nice today', 'declarative'),
         ('who are you and how did you get here', 'interrogative'),
         ('i cant believe that just happened', 'exclamatory'),
         ('youre such an idiot', 'exclamatory'),
         ('would you please go to the market and get me a bagel', 'interrogative'),
         ('the mitochondria is the powerhouse of the cell', 'declarative'),
         ('what does the mitochondria do', 'interrogative')]

test = [('what time is it', 'interrogative'),
        ('can you get me a beer', 'interrogative'),
        ('it is a beautiful day', 'declarative'),
        ('youre a tool', 'declarative'),
        ('the hour grows late and gandalf the gray rides to rohan', 'declarative')]


def find_gradient(pos, tokens):
    x = []
    for i in tokens:
        if i[1] == pos:
            x.append(1)
        else:
            x.append(0)
    y = range(len(x))
    line = linregress(x, y)
    #print(line)
    slope = line[0]
    if np.isnan(slope):
        return 0
    else:
        return slope


def sent2grad(sentence):
    t = nltk.word_tokenize(sentence)
    p = nltk.pos_tag(t)
    gradients = []
    for i in pos_index:
        grad = find_gradient(i, p)
        gradients.append(grad)
    return np.asarray(gradients)


if __name__ == '__main__':
    train_x = []
    train_y = []
    for i in train:
        train_x.append(sent2grad(i[0]))
        train_y.append(i[1])
    model = SVC()
    train_x = np.asarray(train_x)
    model.fit(train_x, train_y)
    for i in test:
        vector = sent2grad(i[0])
        vector = np.asarray(vector).reshape(1, -1)
        pred, = model.predict(vector)
        print('Predicted', pred, '   Actual', i[1])
