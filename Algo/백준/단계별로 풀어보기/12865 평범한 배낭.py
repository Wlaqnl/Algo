import sys
sys.stdin=open("12865 평범한 배낭.txt","r")

N, K = map(int,input().split())
value=[[0]*(K+1) for _ in range(N+1)]

for i in range(1,N+1):
    w,v=map(int,input().split())
    for j in range(1,K+1):
        if j<w:
            value[i][j]=value[i-1][j]
        else:
            value[i][j]=max(value[i-1][j], value[i-1][j-w]+v)
print(value[N][K])