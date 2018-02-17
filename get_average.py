def get_average(tweet_text): 
    scorelist = []
    tokenlist = tweet_text.split()
    for x in tokenlist:
        try:
            scorelist.append(int(x))
        except:
            pass
    return sum(scorelist)/len(scorelist)