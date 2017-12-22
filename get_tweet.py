import tweepy
import settings

def get_tweet():
    auth = tweepy.OAuthHandler(settings.CONSUMER_KEY,settings.CONSUMER_SECRET)
    auth.set_access_token(settings.ACCESS_TOKEN,settings.ACCESS_TOKEN_SECRET)
    api=tweepy.API(auth)

    id="942594709121200128"
    return api.get_status(id).text