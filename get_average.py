def get_average(tweet_text): 
    scorelist = []
    tokenlist = tweet_text.split()
    for x in tokenlist:
        try:
            scorelist.append(int(float(x)))
        except:
            pass
    try:
         return sum(scorelist)/len(scorelist)
    except:
         return "ダマレシネコロスゾ"