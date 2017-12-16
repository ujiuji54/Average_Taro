from get_tweet import get_tweet
from get_score_list import get_score_list

scores=get_score_list()
print(sum(scores)/len(scores))