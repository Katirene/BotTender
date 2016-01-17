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
  print(u'Got {0} results'.format(results.count))

  for tweet in results:
    try:
      print(u'Found tweet id:{0}, from:\"{1}\", \n\t\"{2}\"\n'.format(tweet.id, tweet.user.name, tweet.text))
      #api.update_status("my Update", in_reply_to_status_id = user_id)
    except Exception as ex:
      print ("Error Tweeting.  Error details: {0}".format(ex))