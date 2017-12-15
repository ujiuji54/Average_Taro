import get_tweet
import get_score_list

scores=get_score_list(get_tweet())
print(sum(scores)/len(scores))