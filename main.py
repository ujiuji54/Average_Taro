from get_tweet import get_tweet
from get_average import get_average
from reply import reply

import tweepy
import settings
auth = tweepy.OAuthHandler(settings.CONSUMER_KEY,settings.CONSUMER_SECRET)
auth.set_access_token(settings.ACCESS_TOKEN,settings.ACCESS_TOKEN_SECRET)
api=tweepy.API(auth)

while True:
    for tweet_id in get_tweet(api):
        reply(api,tweet_id,get_average(api.get_status(tweet_id).text))