import tweepy, time, sys
import cvs


CONSUMER_KEY = 
CONSUMER_SECRET = 
ACCESS_KEY = 
ACCESS_SECRET = 
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

api = tweepy.API(auth)
results = api.search_users(q="I need a drink"&since_id=0)

for tweet in results:
	try:
		api.update_status("my Update", in_reply_to_status_id = user_id)
	except:
		print ("Error Tweeting")

time.sleep(900)	