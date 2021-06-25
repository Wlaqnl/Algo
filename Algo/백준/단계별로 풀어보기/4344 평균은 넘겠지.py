import sys
sys.stdin=open("4344 평균은 넘겠지.txt","r")
T=int(input())

for tc in range(T):
    score = list(map(int,input().split()))
    average = sum(score[1:])/score[0]
    #print(average)
    cnt=0

    for i in score[1:]:
        if i>average:
            cnt+=1
    answer=round(cnt/score[0]*100,3)
    print(f"{format(answer,'.3f')}%")
