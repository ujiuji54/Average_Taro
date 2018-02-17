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
    for result in api.search(q = '#あべれーじ太郎',result_type='recent',count = 10):
        if(result.id==latest_tweet_id):break
        tweetlist.append(result.id)

    f = open('latest_id.txt', 'w')
    f.write(str(tweetlist[0]))
    f.close()

    return tweetlist