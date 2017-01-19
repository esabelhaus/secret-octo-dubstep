from __future__ import division
import collections
from nltk.corpus import PlaintextCorpusReader, movie_reviews, stopwords
from nltk.classify import NaiveBayesClassifier
import nltk.classify.util
import nltk.metrics
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
        words.append((word.lower(), True))

    return dict(words)

def movie_words(sentiment):
    negids = movie_reviews.fileids(sentiment)
    words = []
    for file_id in negids:
        for word in movie_reviews.words(file_id):
            words.append(word)
    return words

def evaluate_classifier(featx):
    posids = movie_reviews.fileids('pos')

    print(featx)

    negfeats = []
    posfeats = []

    for w in movie_words('neg'):
        try:
            negfeats.append(featx[w], 'neg')
        except:
            print(w + ' is missing')

    for w in movie_words('pos'):
        try:
            posfeats.append(featx[w], 'pos')
        except:
            print(w + ' is missing')

    print(negfeats)
    print(posfeats)

    negcutoff = len(negfeats)*3/4
    poscutoff = len(posfeats)*3/4

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
    print('pos precision:', nltk.metrics.precision(refsets['pos'], testsets['pos']))
    print('pos recall:', nltk.metrics.recall(refsets['pos'], testsets['pos']))
    print('neg precision:', nltk.metrics.precision(refsets['neg'], testsets['neg']))
    print('neg recall:', nltk.metrics.recall(refsets['neg'], testsets['neg']))
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
