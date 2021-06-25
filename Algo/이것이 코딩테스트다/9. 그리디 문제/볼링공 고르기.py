import sys
sys.stdin=open("볼링공 고르기.txt","r")
T=int(input())

for tc in range(T):
    N, M = map(int,input().split())
    weight = list(map(int,input().split()))
    cnt=0

    for i in range(N-1):
        for j in range(i+1, N):
            if weight[i]!=weight[j]:
                cnt+=1

    print(cnt)