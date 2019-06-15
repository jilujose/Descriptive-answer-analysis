from nltk.corpus import stopwords
from nltk.corpus import wordnet
import difflib as dl
import string
import os
import new
sim = dl.get_close_matches
num = 0
num1 = 0
#----------------------------------------------------------------Teacher-----------------------------------------------------------

os.system("tesseract "+str(new.img)+" st_sheet")

sent1 = open(str(new.tea))  #open teacher key
lines1 = sent1.read()
stop_words = set(stopwords.words('english'))	#calling english stopword list
word_tokens = lines1.split()	#spliting
filtered_sentence1 = [w for w in word_tokens if not w in stop_words]
filtered_sentence1 = []		#saving filtered sentence

for w in word_tokens:
    if w not in stop_words:
        filtered_sentence1.append(w)

newlines = []
for item in filtered_sentence1:  #removing punctuations
   newlines.append(item.strip(',''.''-'))
lines1 = newlines
#----------------------------------------------------------------End Teacher-------------------------------------------------------


#----------------------------------------------------------------Student----------------------------------------------------------
sent2 = open("st_sheet.txt")
lines2 = sent2.read()
stop_words = set(stopwords.words('english'))
word_tokens = lines2.split()
filtered_sentence2 = [w for w in word_tokens if not w in stop_words]
filtered_sentence2 = []

for w in word_tokens:
    if w not in stop_words:
        filtered_sentence2.append(w)
newlines = []
for item in filtered_sentence2:  #removing punctuations
   newlines.append(item.strip(',''.'))
lines2 = newlines       
#----------------------------------------------------------------End Student-------------------------------------------------------


#----------------------------------------------------------------synset-----------------------------------------------------------
syns = {w : [] for w in lines1}

for k, v in syns.items():
    for synset in wordnet.synsets(k):
        for lemma in synset.lemmas():
            v.append(lemma.name())

#----------------------------------------------------------------synset-----------------------------------------------------------

#----------------------------------------------------------------Compare-----------------------------------------------------------            
for i in syns:
    if sim(i, lines2):
        num1 += 1
for j in lines1:
    if sim(j, lines2):
        num += 1
n = float(num+num1) / float((len(lines1)+num1))
print "The Student is awarded"
print '%d%% Marks' % int(n * 100)

#----------------------------------------------------------------End Compare-------------------------------------------------------