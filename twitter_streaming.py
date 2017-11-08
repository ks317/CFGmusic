try:
    import json
except ImportError:
    import simplejson as json

# Import the necessary methods from "twitter" library
from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream

# Variables that contains the user credentials to access Twitter API 
ACCESS_TOKEN = '2427197298-yKTWJHuv8wepyLf6bPaxJyLaQccuALsJGcxdHbV'
ACCESS_SECRET = 'K62gmO2hSrryDUdZFkeH1vTZxFRQCs9PQByrn7IcjMupq'
CONSUMER_KEY = 'sh4qaKmQbCPvyePQUXz9Pqdq8'
CONSUMER_SECRET = 'HaCnOHHOwt1AIgDUgNzNZ72V745UbVhlFrbBTg9pjeli5O1JvJ'

def get_songs(hashtag):
	oauth = OAuth(ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET)
	# Initiate the connection to Twitter Streaming API
	twitter_stream = Twitter(auth=oauth)
	# Get a sample of the public data following through Twitter
	iterator = twitter_stream.search.tweets(q=hashtag)
	
	for status in iterator["statuses"]:
		print "The tweet is : " + status["text"]
		print "The hashtags are: "
		print status["entities"]["hashtags"]
		print "Created at: " + status["created_at"]
	
	tweet_count = 10
	for tweet in iterator:
		tweet_count -= 1
    # Twitter Python Tool wraps the data returned by Twitter 
    # as a TwitterDictResponse object.
    # We convert it back to the JSON format to print/score
		print json.dumps(tweet)  
       
		if tweet_count <= 0:
			break 
	
get_songs('brexit')
