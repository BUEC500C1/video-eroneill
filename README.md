## Erin O'Neill
### Copyright 2020 erinkate@bu.edu

# Multitasking
Main Exercise:  Using the twitter feed, construct a daily video summarizing a twitter handle day

-Convert text into an image in a frame

-Do a sequence of all texts and images in chronological order.

-Display each video frame for 3 seconds

# Twitter work
To run twitter image creation simply run twitter_work.py - currently have the BUCollegeofENG twitter account hard coded 
this could be changed easily in this python file.  

This file outputs 100 images with the last 100 tweets.  These images are saved in the twitter_images subfolder.  They write over the files that are there so save any old images you want. 

To create a video, simply input the username with all the images to the createtweetvideo.py file 
(ie python createtweetvideo.py username) to get a video of the last 100 tweets by this user 
