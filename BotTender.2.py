#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tweepy, time, sys

argfile = str(sys.argv[1])


# build savepoint path + file
hashedHashtag = hashlib.md5(hashtag).hexdigest()
last_id_filename = "last_id_hashtag_%s" % hashedHashtag
##rt_bot_path = os.path.dirname(os.path.abspath(__file__))
##last_id_file = os.path.join(rt_bot_path, last_id_filename)

#enter the corresponding information from your Twitter application:
CONSUMER_KEY = '1234abcd...'#keep the quotes, replace this with your consumer key
CONSUMER_SECRET = '1234abcd...'#keep the quotes, replace this with your consumer secret key
ACCESS_KEY = '1234abcd...'#keep the quotes, replace this with your access token
ACCESS_SECRET = '1234abcd...'#keep the quotes, replace this with your access token secret
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

filename=open(argfile,'r')
f=filename.readlines()
filename.close()


# retrieve last savepoint if available
try:
	with open(last_id_file, "r") as file:
		savepoint = file.read()
except IOError:
	savepoint = ""
	print "No savepoint found. Trying to get as many results as possible."
# search query
timelineIterator = tweepy.Cursor(api.search, q="I need a drink", since_id=savepoint, lang=tweetLanguage).items()

# put everything into a list to be able to sort/filter
timeline = []
for status in timelineIterator:
	timeline.append(status)

try:
    last_tweet_id = timeline[0].id
except IndexError:
    last_tweet_id = savepoint

for line in f:
    api.update_status(line)
    time.sleep(900)#Tweet every 15 minutes

