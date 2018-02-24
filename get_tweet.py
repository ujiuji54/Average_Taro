import tweepy

def get_tweet(api):
    f = open('latest_id.txt', 'r')
    latest_tweet_id = f.readline()
    f.close()

    try:
        timeline = api.home_timeline(count=100,since_id=latest_tweet_id,exclude_replies=True)
    except:
        print("api limit home_timeline()")
        timeline = []
    tweetlist = []

    for tweet in reversed(timeline):
        print(tweet.text+"\n")
        if tweet.text.find("#あべれーじ太郎") > -1:
            tweetlist.append(tweet.id)

    f = open('latest_id.txt', 'w')
    try:
        f.write(str(timeline[0].id))
    except:
        f.write(latest_tweet_id)
        print("Wating...")
    f.close()

    return tweetlist