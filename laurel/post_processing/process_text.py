from __future__ import division
from nltk.corpus import PlaintextCorpusReader
from nltk.corpus import stopwords
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
    stopwords = nltk.corpus.stopwords.words('english')
    content = [w for w in text if w.lower() not in stopwords]
    return len(content) / len(text)

# list words in files of corpus
for file_id in wordlists.fileids():
    print(wordlists.words(file_id))

# this is going to be neat once it's working
# I will tokenize all sentences and words, then generate a laurel corpus :)

# # how many sentences in corpus
# tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
# tokenized_corpus = tokenizer.tokenize(wordlists.sents()))
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

print(nltk.classify.accuracy(classifier, test_set))
