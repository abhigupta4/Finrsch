from nltk.corpus import PlaintextCorpusReader
corpus_root = 'Test/'
wordlists = PlaintextCorpusReader(corpus_root, '.*')
print wordlists.fileids()
print wordlists.categories()