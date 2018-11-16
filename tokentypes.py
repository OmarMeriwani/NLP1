import nltk
import re
import requests
from bs4 import BeautifulSoup as bs
import html2text
from nltk import hmm
from nltk.corpus import brown
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.stem import PorterStemmer
from nltk.stem import LancasterStemmer
from nltk import pos_tag


h = html2text.HTML2Text()
h.ignore_links = True
link = "https://www.theguardian.com/music/2018/oct/19/while-my-guitar-gently-weeps-beatles-george-harrison"
#Get link's HTML contents
f = requests.get(link)
#Convert
h = html2text.HTML2Text()
h.ignore_links = True
htext = h.handle(f.text)
#To read guardian articles the lines between the beginning symbol (#) and the word Topics only should be taken
htext = htext[htext.find('# '):htext.find('Topics')]
htext.replace('#  ','')
htext_lines = htext.splitlines()
counter  = 0
newlines = []
for line in htext_lines:
    #To ignore the image link and caption, social media tags and empty lines
    if (counter < 3 or counter > 20) and (line != '' and line != 'Facebook Twitter Pinterest' ):
        newlines.append(line)
    counter+=1
htext = '\n'.join(newlines)
#Now the text is ready
print(htext)

first_tokens = nltk.word_tokenize(htext)
print('Tokens before lowercasing before lemmatization:', len(first_tokens))
print(first_tokens)
print('Types before lowercasing before lemmatization:', len(set(first_tokens)))
print(set(first_tokens))

first_tokens = [token.lower() for token in first_tokens]
print('Tokens after lowercasing before lemmatization:', len(first_tokens))
print(first_tokens)
print('Types after lowercasing before lemmatization:', len(set(first_tokens)))
print(set(first_tokens))
lmtzr = WordNetLemmatizer()
second_tokens = [lmtzr.lemmatize(line) for line in first_tokens]
print('Tokens after lemmatization:', len(second_tokens))
print(second_tokens)
print('Types after lemmatization:', len(set(second_tokens)))
print(set(second_tokens))
unitag = nltk.tag.UnigramTagger(brown.tagged_sents(categories = 'news'))
unitagg = unitag.tag(second_tokens)
print('POS Tagging:')
print(unitagg)
print ('Errors:', 'gently: None (Correct: RB), ', 'weeps: None (Correct: VB), ', 'acoustic: None (Correct: JJ), ', 'george: None (Correct: NN)')