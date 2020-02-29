# EC500 Hw3
# Copyright 2020  Erin K O'Neill erinkate@bu.edu

# convert twitter username to video

import tweepy
import json
import os 
import string
import sys
import textwrap
from key_reader import key_get

def setup_keys(self):
	key = key_get()
	auth = tweepy.OAuthHandler(key.consumer_key, key.consumer_secret)
	auth.set_access_token(key.access_key, key.access_secret)

    authinp = tweepy.API(auth)

	return authinp

def get_username_tweets(authinp, username):
    try:
        tweets = authinp.user_timeline(screen_name=username, count=20)
        return tweets
    except tweepy.error.TweepError as e:
        print(e)
        return ""

def clean_up_tweet(tweettotal)
	new_tweet = []
	for tweetugly in tweettotal:
	    tweetugly = re.sub(r'@[A-Za-z0-9_]+','',tweetugly) #remove username
        tweet = re.sub(r"http\S+", "", tweetugly) #remove link
        # tweet = re.sub(r"(”|“|-|\+|`|#|,|;|\|)*", "", tweetugly) #remove extra punctuation
        tweet = re.sub(r"&amp", "", tweetugly) #should remove emoji
        new_tweet.append(tweet)
    return new_tweet