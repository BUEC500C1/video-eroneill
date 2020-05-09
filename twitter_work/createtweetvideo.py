# EC500 Hw3
# Copyright 2020  Erin K O'Neill erinkate@bu.edu

# convert twitter username to video

import glob
import string 
import ffmpeg
from twitter_work import tweetprocessing
from sys import argv

def main():
	username = argv[1]
	# print(username, "is my username")
	tweetprocessing(username)
	fileName = './' + username + '_pics/' + '*.png'
	videoName = './' + username + '_pics/' + username + "_summary.mp4"

	ffmpeg.input(fileName, pattern_type = 'glob', framerate = 0.33).output(videoName).run()
	print('processing complete')

if __name__ == '__main__':
    main()
