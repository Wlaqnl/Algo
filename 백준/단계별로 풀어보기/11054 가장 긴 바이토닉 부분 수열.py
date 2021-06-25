import sys
sys.stdin=open("11054 가장 긴 바이토닉 부분 수열.txt","r")

n=int(input())
num=list(map(int,input().split()))

dp_1=[0 for _ in range(n)]
dp_2=[0 for _ in range(n)]
dp=[0 for _ in range(n)]

for i in range(n):
    for j in range(i):
        if num[i]>num[j] and dp_1[i]<dp_1[j]:
            dp_1[i]=dp_1[j]
    dp_1[i]+=1

for i in range(n-1, -1, -1):
    for j in range(n-1, i, -1):
        if num[i]>num[j] and dp_2[i]<dp_2[j]:
            dp_2[i]=dp_2[j]
    dp_2[i]+=1

for i in range(n):
    dp[i]=dp_1[i]+dp_2[i]-1
print(max(dp))
