import sys
sys.stdin=open("럭키 스트레이트.txt","r")
T=int(input())

for tc in range(T):
    score=str(input())
    n=len(score)
    a=score[:n//2]
    b=score[n//2:]
    score_a=0
    score_b=0

    for i in range(n//2):
        score_a+=int(a[i])
        score_b+=int(b[i])

    if score_a==score_b:
        print("LUCKY")
    else:
        print("READY")