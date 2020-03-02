# Erin O'Neill 
# EC500

from twitter_work import tweetprocessing
import threading 
import queue 
import multiprocessing 


def twitter_setup(queued):
	while True: #will want a way out of this loop - this is it 
		user = queued.get()

		if user is None: break 

		tweetprocessing(user)

		queued.task_done()




# just going to grab the usernames and queue them 

def queue_twitter_jobs(username):
	q1 = queue.Queue(maxsize=5)

	#now thread the queue 
	threadhead = threading.Thread(name="Process:" + "base", target=twitter_setup, args(q1,))
	threadhead.start()

	q1.put(username)