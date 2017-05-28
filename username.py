import tweepy
import csv
import pandas as pd
import numpy as np


reader = csv.reader(open('socal_tweet_12location_edit.csv', 'rU'))
consumer_key = 'T6ZIs9sys0EnRS1i94x9iFHF0'
consumer_secret = 'mfke4em8sFv0IsO0pwj8oL2yfpmjoYftA6jRL97lrOiGtXcCA5'
access_token = '3997699152-iFgooSVOG27s0bumPsRWkkhbyPNkvns3Z8eYSse'
access_token_secret ='c13p1ufeDHLwf5YkcLxZS0ql4QlcXen2BY4vfdutWVbFT'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

column = [row[8] for row in reader]
un=[]
for col in column[1:]:
	try:
		user = api.get_user(screen_name=col)
		a,b=user.name.split(' ', 1)
		print a
		un.append(a)
  except:
		un.append("no name")

df = pd.read_csv('socal_tweet_12location_edit.csv')
new_column = pd.DataFrame({'firstname': un})
df = df.merge(new_column, left_index = True, right_index = True)
df.to_csv('socal_tweet_12location_edit.csv')
