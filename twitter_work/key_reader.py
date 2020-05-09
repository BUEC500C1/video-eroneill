# EC500 Hw3
# Copyright 2020  Erin K O'Neill erinkate@bu.edu

# convert twitter key to auth

class twitter_key():
    def __init__(self, keys):
        self.consumer_key = keys[0]
        self.consumer_secret = keys[1]
        self.access_key = keys[2]
        self.access_secret = keys[3]
        
def key_get():
    keys = ("1", "2", "3", "4")
    mykey = twitter_key(keys)
    print(mykey.consumer_secret)