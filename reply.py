import tweepy
import settings

def reply(tweet_id,average):
    auth = tweepy.OAuthHandler(settings.CONSUMER_KEY,settings.CONSUMER_SECRET)
    auth.set_access_token(settings.ACCESS_TOKEN,settings.ACCESS_TOKEN_SECRET)
    api=tweepy.API(auth)

    reply_tweet = "@" + str(api.get_status(tweet_id).user.screen_name) +" "+ str(average)
    print(reply_tweet)
    api.update_status(status=reply_tweet, in_repry_to_status_id=tweet_id)