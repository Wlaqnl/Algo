import sys
sys.stdin=open("2293 동전1.txt","r")

N, K = map(int,input().split())
coin=[int(input()) for _ in range(N)]

dp=[0 for i in range(10001)]
dp[0]=1

for c in coin:
    for j in range(c,K+1):
        dp[j]+=dp[j-c]

print(dp[K])
