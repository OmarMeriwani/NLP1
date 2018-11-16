import nltk
import csv
import re
import urllib
import requests
from bs4 import BeautifulSoup as bs
import html2text
reg = r'(\+|00|\+ |00 |0||0 )( ?|-?)(\d{1}|\d{2}|\d{3}|\d{4}|\d{5}|\d{6})( ?|-?)(\(0\))?( ?||-?)(\(?)(\d{6}|\d{5}|\d{4}|\d{3}|\d{2})?(\)?)( ?||-?)(\d{5}|\d{4}|\d{3}|\d{2})( ?||-?)(\d{5}|\d{4}|\d{3}|\d{2})( ?||-?)(\d{5}|\d{4}|\d{3}|\d{2})'
with open('d:\phoneNumbers.csv',mode='r') as csvFile:
    csv_reader = csv.DictReader(csvFile)
    '''for  vall in csv_reader:
        a = re.match(reg, str(vall["PhoneNumber"]))
        if a != None :
            # print (str(a.string), '::', vall["PhoneNumber"])
            if str(vall["PhoneNumber"]) == str(a.string):
                print('Complete', a.string)
            else:
                print('Incomplete', vall,'::', a.group())
        else:
            print('Not found ', vall["PhoneNumber"])'''
link2 = "https://www.halifax.co.uk/contactus/call-us/"
link = "https://personal.natwest.com/personal/support-centre/contact-us.html"
f = requests.get(link)
#print(f.text)
h = html2text.HTML2Text()
h.ignore_links = True
htext = h.handle(f.text)
#print (htext)
r1 = re.findall(reg,htext)
r2 = re.findall(reg,"""
**+44 (0) 1733 573 189**
TRUE: plus sign - no space - international code - (0) - 10 digits           +44 (0) 223 279 8302
TRUE: plus sign - no space - international code - no spcs - 10 digits       +964(0)3332 798 302
TRUE: plus sign - no space - international code - no optional - 10 digits   +964 3334 798 302
TRUE: plus sign - no space - international code - no space - 10 digits      +9663334 798 302
TRUE: Just a group of space separ chunks of numbers with 0 in the beginning 009663334 798 302
TRUE: Just a group of numbers with 00 in the beginning                      0093334798302
TRUE: Just a group of numbers with 0 in the beginning                       013334798302
TRUE: Just a group of numbers without 0 in the beginning                    13334798302
TRUE: zero - one digit - different place of optional code                   01(333)4798302
FALSE: just a space separated numbers                                       0 1 3 3 3 4 7 9 8 3 0 2
FALSE: 5 digits number                                                      44445
FALSE: 6 digits number                                                       444456
TRUE: 8 digits number                                                       4444568
TRUE:                                                                       +44(0)113 279 8302
TRUE:                                                                       +44 5679401945
""")
print(r1)

result1 = ""
for line in r1:
    print ('Found a match!\nPhone number:',''.join(str(r) for v in line for r in v))

#print(result1)

'''lines = re.compile(r'\r\n|\r|\n|\s\s|[A-Za-z]|!,#$%_*').split(result1)
for m in lines:
    print("Matched:" , m)'''

