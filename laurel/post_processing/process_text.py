from __future__ import division
import collections
from nltk.corpus import PlaintextCorpusReader, movie_reviews, stopwords
from nltk.classify import NaiveBayesClassifier
import nltk.classify.util
from nltk.metrics import *
from nltk import precision
from nltk import recall
from os import path

dir_path = path.dirname(path.realpath(__file__))
corpus_root = dir_path + '/../processed'

wordlists = PlaintextCorpusReader(corpus_root, '.*')

#print(wordlists.fileids())

def lexical_diversity(text):
    return len(text) / len(set(text))

def pos_features(sentence, i):
    features = {"suffix(1)": sentence[i][-1:],
                "suffix(2)": sentence[i][-2:],
                "suffix(3)": sentence[i][-3:]}
    if i == 0:
        features["prev-word"] = "<START>"
    else:
        features["prev-word"] = sentence[i-1]
    return features

def content_fraction(text):
    stopwords = stopwords.words('english')
    content = [w for w in text if w.lower() not in stopwords]
    return len(content) / len(text)

def stopword_filtered_word_feats():
    return dict([(word, True) for word in wordlists.words() if word not in stopset])

def word_feats():
    words = []
    for word in wordlists.words():
        words.append(word.lower())

    return words

def movie_words(sentiment):
    sentiment_words = movie_reviews.fileids(sentiment)
    words = {}
    for file_id in sentiment_words:
        for word in movie_reviews.words(file_id):
            words[word.lower()] = True

    return words

def evaluate_classifier(featx):
    #print(featx)
    neg_dict = movie_words('neg')
    pos_dict = movie_words('pos')

    negfeats = []
    posfeats = []
    for word in featx:
        try:
            neg_dict[word]
            negfeats.append(({word: True}, 'neg'))
        except KeyError:
            print(word + " Missing from negative")

        try:
            pos_dict[word]
            posfeats.append(({word: True}, 'neg'))
        except KeyError:
            print(word + " Missing from positive")

    negcutoff = len(negfeats)*3//4
    poscutoff = len(posfeats)*3//4

    print(negcutoff)
    print(poscutoff)

    trainfeats = negfeats[:negcutoff] + posfeats[:poscutoff]
    testfeats = negfeats[negcutoff:] + posfeats[poscutoff:]

    classifier = NaiveBayesClassifier.train(trainfeats)
    refsets = collections.defaultdict(set)
    testsets = collections.defaultdict(set)

    for i, (feats, label) in enumerate(testfeats):
            refsets[label].add(i)
            observed = classifier.classify(feats)
            testsets[observed].add(i)

    print('accuracy:', nltk.classify.util.accuracy(classifier, testfeats))
    print('pos precision:', precision(refsets['pos'], testsets['pos']))
    print('pos recall:', recall(refsets['pos'], testsets['pos']))
    print('neg precision:', precision(refsets['neg'], testsets['neg']))
    print('neg recall:', recall(refsets['neg'], testsets['neg']))
    classifier.show_most_informative_features()

evaluate_classifier(word_feats())

#for file_id in wordlists.fileids():
#    #print()
#    words = list(wordlists.words(file_id))
#    evaluate_classifier(words)

#
# tagged_sents = wordlists.tagged_sents(categories='people')
# featuresets = []
# for tagged_sent in tagged_sents:
#     untagged_sent = nltk.tag.untag(tagged_sent)
#     for i, (word, tag) in enumerate(tagged_sent):
#         featuresets.append( (pos_features(untagged_sent, i), tag) )
#
# size = int(len(featuresets) * 0.1)
# train_set, test_set = featuresets[size:], featuresets[:size]
# classifier = nltk.NaiveBayesClassifier.train(train_set)
#
# print(nltk.classify.accuracy(classifier, test_set))
