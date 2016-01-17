import tweepy, time, sys

execfile('secrets.py')

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

api = tweepy.API(auth)
results = None;

try:
  results = api.search(q="I need a drink")
except:
  print('Error while searching')

if results is not None:
  print('Got {0} results'.format(results.count))

  for tweet in results:
    try:
      print('okay')
      #api.update_status("my Update", in_reply_to_status_id = user_id)
    except:
      print ("Error Tweeting")

  time.sleep(900) 