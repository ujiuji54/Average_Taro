def get_score_list(tweet):  
    list1 = tweet.splitlines()
    list2 = list(map(int,list1))
    print(list2)
    return list2