import tweepy
import csv
import pandas as pd
import numpy as np

#access to twitter
consumer_key = 'consumer_key'
consumer_secret = 'consumer_secret'
access_token = 'access_token '
access_token_secret ='access_token_secret'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
try:
	#col is twitter id 
	user = api.get_user(col)
	a,b=user.name.split(' ', 1)
	print a
		
except:
	print "no name"


