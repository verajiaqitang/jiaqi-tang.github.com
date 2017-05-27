import nltk,csv,numpy 
import sys

from nltk.sentiment.vader import SentimentIntensityAnalyzer as SIA
from nltk import sent_tokenize, word_tokenize, pos_tag
import nltk.classify.util
from nltk.classify import apply_features
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import PlaintextCorpusReader
from nltk.corpus import subjectivity
from nltk.sentiment.util import *
import pandas as pd


reader = csv.reader(open('qiqi2.csv', 'rU'))
column = [row[2] for row in reader]

sent_tokenizer=nltk.data.load('tokenizers/punkt/english.pickle')
sents=[sent_tokenizer.tokenize(str(col)) for col in column ]

sid = SIA()

score=[]
polarity=[]

for sentence in sents:
	print(sentence)
	ss = sid.polarity_scores(str(sentence)) 
	if ss["compound"]>0.0:
			p="positive"
	elif ss["compound"]==0.0:
			p="netural"
	else:
			p="negtive"
	print p
	polarity.append(p)
	score.append(ss["compound"])
	for k in sorted(ss):
		print k,ss[k]



df = pd.read_csv('qiqi2.csv')
new_column = pd.DataFrame({'Scores': score})
df = df.merge(new_column, left_index = True, right_index = True)
new_column2= pd.DataFrame({'Polarity': polarity})
df = df.merge(new_column2, left_index = True, right_index = True)
df.to_csv('qiqi2.csv')
