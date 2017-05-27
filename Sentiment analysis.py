import nltk,csv,numpy 
import sys

from nltk.sentiment.vader import SentimentIntensityAnalyzer as SIA
from nltk import sent_tokenize, word_tokenize, pos_tag
import nltk.classify.util
from nltk.classify import apply_features
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import PlaintextCorpusReader
from nltk.corpus import subjectivity
#from nltk.sentiment import SentimentAnalyzer as SIA
from nltk.sentiment.util import *
import pandas as pd

#files = ".*\.txt"
reader = csv.reader(open('qiqi2.csv', 'rU'))
#writer = csv.writer(open('qiqi.csv', 'w'))
#with open('qiqi.csv', 'ab') as csvfile:
	#fieldnames = ['Score','Polarity']
	#writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
column = [row[2] for row in reader]

#row0 = r.next()
#row0.append('scores')
#row0 = r.next()
#row0.append('polarity')
#writer.writerow(row+['scores'])
#writer.writerow(row+['polarity'])
#def gender_features(word):
	#return {'last_letter': word[-1]}
#tokenData = nltk.word_tokenize(str(column))
#set(w.lower() for w in tokenData)
#porter = nltk.PorterStemmer()
#set(porter.stem(t) for t in tokenData)
#lancaster = nltk.LancasterStemmer()
#porter.stem(t) for t in tokenData
#wnl = nltk.WordNetLemmatizer()
#wnl.lemmatize(t) for t in tokenData
sent_tokenizer=nltk.data.load('tokenizers/punkt/english.pickle')
sents=[sent_tokenizer.tokenize(str(col)) for col in column ]
#print sents
sid = SIA()
#sentry="Janna is a stupid "
#stry=sid.polarity_scores(sentry)

#print "the score is "+ str(stry["compound"])
#print "So the sentence of "+sentry+"is" +" "+p +"!!!!!!"
score=[]
polarity=[]
#write = csv.writer(open('qiqiqi.csv', 'w'))
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
	#print()


df = pd.read_csv('qiqi2.csv')
new_column = pd.DataFrame({'Scores': score})
df = df.merge(new_column, left_index = True, right_index = True)
new_column2= pd.DataFrame({'Polarity': polarity})
df = df.merge(new_column2, left_index = True, right_index = True)
df.to_csv('qiqi2.csv')


#for row in data:
    #if counter[row[0]] >= 4:
        #writer.writerow(row)
#print len(sents)
#gender_feature/
#train_set=sents[:16]/
#train_set = apply_features(gender_features, names[500:])
#test_set = apply_features(gender_features, names[:500])
#classifier = nltk.NaiveBayesClassifier.train(train_set)/
#output_file = open('~\Downloads\outputnltk.txt', 'w'
