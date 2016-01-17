import tweepy, sys
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import time

CONSUMER_KEY = 
CONSUMER_SECRET = 
ACCESS_KEY = 
ACCESS_SECRET = 
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

class listener(StreamListener):

    def on_data(self, data):
      try:
          print data
          saveFile = open('StreamingBotResults.csv','a')
          saveFile.write(data)
          saveFile.write('\n')
          saveFile.close()
          return True
      except BaseException, e:
          print 'failed ondata',str(e)
          time.sleep(5)

    def on_error(self, status):
        print status


auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
twitterStream = Stream(auth, listener())
twitterStream.filter(track=["I need a drink"],languages='en')