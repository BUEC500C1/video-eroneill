# EC500 Hw3
# Copyright 2020  Erin K O'Neill erinkate@bu.edu

# convert twitter username to video

import json
import tweepy
import textwrap
import os
import re
import string
from key_reader import key_get
from PIL import Image, ImageDraw, ImageFont

def setup_keys():
	key = key_get()
	auth = tweepy.OAuthHandler(key.consumer_key, key.consumer_secret)
	auth.set_access_token(key.access_key, key.access_secret)
	authinp = tweepy.API(auth, parser=tweepy.parsers.JSONParser())
	return authinp

def get_username_tweets(authinp, username):
    try:
        tweets = authinp.user_timeline(screen_name=username, count=100, tweet_mode='extended')
        json.dumps(tweets)
        return tweets
    except tweepy.error.TweepError as e:
        print(e)
        return ""

def clean_up_tweet(tweettotal, username):
	new_tweet = []
	username = '@' + username
	for tweetugly in tweettotal: 
		tweet = tweetugly['full_text']
		tweet = tweet.replace(username,"") #remove username
		tweet = tweet.replace("\n", " ")
		tweet = re.sub(r"http\S+", "", tweet) #remove link
		printable = set(string.printable)
		filter(lambda x: x in printable, tweet)
		tweet = str(tweet.encode('ascii', 'ignore'))
		# print("this is my tweet", tweet)
		new_tweet.append(tweet)
	return new_tweet

def createPics(new_tweet, username):
	if not os.path.isdir(username + '_pics'):
		os.mkdir(username + '_pics')
	font = ImageFont.truetype('C:\Windows\Fonts\Calibri.ttf', 32)
	blank = Image.new('RGBA', (1024, 768), (255,255,255,255)) # default to white background
	countforimg = 1 # this is just to count for filenaming 
	for tweet in new_tweet:
		blank = Image.new('RGBA', (1024, 768), (255,255,255,255)) # default to white background
		image = ImageDraw.Draw(blank)
		wrapper = textwrap.TextWrapper(width=50) 
		tweet_list = wrapper.wrap(text=tweet)
		yloc = 200
		image.text((200, 100), username, font= font, fill="#000") 
		for line in tweet_list:
			image.text((200,yloc), line, font = font, fill="#000", align="center")
			yloc = yloc + 50

		filename = './'+ str(username) + '_pics/' +str(countforimg)+'.png'
		blank.save(filename)
		countforimg += 1
	return 1 

def tweetprocessing(username):
	keyset = setup_keys()
	origtweet = get_username_tweets(keyset, username)
	cleantweet = clean_up_tweet(origtweet, username)
	createPics(cleantweet, username)
	return 1 

def main():
	username = "BUCollegeofENG"
	tweetprocessing(username)
	# tweets = get_username_tweets(authinp, username)
	# print(tweets[0])
	print('test passed')

if __name__ == '__main__':
    main()
