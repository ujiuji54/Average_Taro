import tweepy
import settings

def get_tweet():
    auth = tweepy.OAuthHandler(settings.CONSUMER_KEY,settings.CONSUMER_SECRET)
    auth.set_access_token(settings.ACCESS_TOKEN,settings.ACCESS_TOKEN_SECRET)
    api=tweepy.API(auth)

    id = 0
    tweetlist = []
    word = "#あべれーじ太郎"
    
    for result in api.search(q = word,result_type='recent',count = 10):
        if(result.id==id):break
        tweetlist.append(result.id)
        id=result.id
    return tweetlist