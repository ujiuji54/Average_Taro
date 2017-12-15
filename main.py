scores=[]
score = int(input())
while score >= 0:
    scores.append(score)
    score=int(input())
print(sum(scores)/len(scores))