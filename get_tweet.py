import tweepy
import settings

def get_tweet():
    auth = tweepy.OAuthHandler(settings.CONSUMER_KEY,settings.CONSUMER_SECRET)
    auth.set_access_token(settings.ACCESS_TOKEN,settings.ACCESS_TOKEN_SECRET)
    api=tweepy.API(auth)

    f = open('latest_id.txt', 'r')
    latest_tweet_id = f.readline()
    f.close()

    tweetlist = []
    for result in api.mentions_timeline(since_id=latest_tweet_id,count = 100):
        tweetlist.append(result.id)

    f = open('latest_id.txt', 'w')
    try:
        f.write(str(tweetlist[0]))
    except:
        print("latest")
        f.write(latest_tweet_id)
    f.close()

    return tweetlist