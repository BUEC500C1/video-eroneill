# EC500 Hw3
# Copyright 2020  Erin K O'Neill erinkate@bu.edu

# convert twitter username to video

import tweepy
from key_reader import key_get
from PIL import Image, ImageDraw, ImageFont

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

def clean_up_tweet(tweettotal):
	new_tweet = []
	for tweetugly in tweettotal:
	    tweetugly = re.sub(r'@[A-Za-z0-9_]+','',tweetugly) #remove username
        tweet = re.sub(r"http\S+", "", tweetugly) #remove link
        tweet = re.sub(r"&amp", "", tweetugly) #should remove emoji
        new_tweet.append(tweet)
	return new_tweet

def createPics(new_tweet):
	font = ImageFont.truetype('/Library/Fonts/Calibri.ttf', 40)
	blank = Image.new('RGBA', (1024, 768), (255,255,255,255)) # default to white background
	countforimg = 0 # this is just to count for filenaming 
	for tweet in new_tweet:
		image = ImageDraw.Draw(blank)
		draw.text((50,100), tweet, font = font)
		image.save('./tweet_images/'+str(countforimg)+'.png')
		countforimg += 1
	return 1 

def tweetprocessing(username):
	keyset = setup_keys()
	origtweet = get_username_tweets(keyset, username)
	cleantweet = clean_up_tweet(origtweet)
	createPics(cleantweet)
	return 1 

def main():
    print(get_username_tweets(erinkateoneill))

if __name__ == '__main__':
    main()