import tweepy

def reply(api,tweet_id,average):
    reply_tweet = "@" + str(api.get_status(tweet_id).user.screen_name) +" "+ str(average)
    print(reply_tweet)
    api.update_status(status=reply_tweet, in_repry_to_status_id=tweet_id)