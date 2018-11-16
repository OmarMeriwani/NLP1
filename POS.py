import nltk
#from nltk.book import *
from nltk.corpus import treebank
from nltk.corpus import brown
from nltk import  word_tokenize
from nltk import hmm
#nltk.help.upenn_tagset("NN*")
files = treebank.fileids()
#print(files)
t = treebank.tagged_words("wsj_0003.mrg")
#for p in t:
    #print(p)

#race1 = nltk.tag.str2tuple('race/NN')
#race2 = nltk.tag.str2tuple('race/VB')
#print(race1)

#print(brown.tagged_words().count(race1))
#print(brown.tagged_words().count(race2))

unitag = nltk.tag.UnigramTagger(brown.tagged_sents(categories = 'news')[:5000])
print (unitag)
s = "The secretariat is expected to race tomorrow."
s_tok = word_tokenize(s)
tt = unitag.tag(s_tok)
print (tt)

hmmTagger = nltk.hmm.HiddenMarkovModelTrainer().train_supervised(brown.tagged_sents(categories="news")[:5000])
tt2 = hmmTagger.tag(s_tok)
print (tt2)