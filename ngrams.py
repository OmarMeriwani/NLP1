from nltk import ngrams
from nltk import word_tokenize
from collections import Counter
import itertools
from nltk.probability import LaplaceProbDist
from nltk import  probability
from nltk.probability import FreqDist
from nltk import bigrams
from nltk import ConditionalFreqDist

print('=========== UNIGRAMS ===========')
#getting main text file
file = open('sampledata.txt','r')
filetext = file.read()
#Cleaning the text from the unwanted characters, other methods like regular expression are applicable but this one is easier
filetext = filetext.replace('<s>','')
filetext =filetext.replace('</s>','')
filetext =filetext.replace('-','')
tokens = word_tokenize(filetext)
print(tokens)
#Getting the vocabulary
file = open('sampledata.vocab.txt','r')
filetext = file.read()
vocab = word_tokenize(filetext)
print(vocab)

fr = FreqDist(tokens)
print('X     |       P(X)')
print('___________________')
for s in fr.items():
    for d in vocab:
        if d == s[0]:
            print(d,'    |       ',(s[1]/len(tokens)).__round__(2))
UNK = 0;
for d in vocab:
    r = [item for item in fr if item[0] != d]
    isemp =  not all(r)
    if isemp == True:
        UNK += (r[1]/len(tokens)).__round__(2)
print('UNK   |       ', UNK)
print('== UNIGRAMS AFTER LAPLACE SMOOTHING ==')
lpt = LaplaceProbDist(fr)
print('X     |       P(X)')
print('___________________')
for d in vocab:
    print(d,'    |       ',lpt.prob(d).__round__(2))
UNK = 0;
for d in vocab:
    r = [item for item in lpt.freqdist().items() if item[0] != d]
    isemp =  not all(r)
    if isemp == True:
        UNK += lpt.prob(r[0])
print('UNK   |       ', UNK)
print('=========== BIGRAMS ===========')
file = open('sampledata.txt','r')
filetext = file.read()
filetext =filetext.replace('</s>','')
filetext =filetext.replace('<s>','')
tokens = word_tokenize(filetext)
tokens.append('<s>')
print(set(tokens))
vocab2 = vocab
vocab2.append('</s>')
vocab2.append('UTK')
big = bigrams(tokens)
cfds = ConditionalFreqDist((w0, w1) for w0, w1 in big)
print(cfds.items())
for v3 in vocab2:
    Unk2 = 0
    fr2 = cfds.get(v3)
    if (fr2 != None):
        for i in fr2.items():
            unigramCount = 0
            for s in fr.items():
                if v3 == s[0]:
                    unigramCount = s[1]
            print('P('+ v3 +'|'+ str(i[0]) +') = ' + str((i[1] / unigramCount).__round__(2)))
    else:
        Unk2 += 1
    print('P(' + v3 + '|UNK) = ' + str(Unk2))
print('======= BIGRAMS SMOOTHING =======')
for v3 in vocab2:
    Unk2 = 0
    fr2 = cfds.get(v3)
    if (fr2 != None):
        for i in fr2.items():
            unigramCount = 0
            for s in fr.items():
                if v3 == s[0]:
                    unigramCount = s[1]
            print('P('+ v3 +'|'+ str(i[0]) +') = ' + str((i[1] / (unigramCount + len(fr.items()))).__round__(2)))
    else:
        Unk2 += 1
    print('P(' + v3 + '|UNK) = ' + str(Unk2))
print('================================')