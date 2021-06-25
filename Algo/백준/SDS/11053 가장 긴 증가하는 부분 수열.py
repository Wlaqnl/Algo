import sys
sys.stdin=open("11053 가장 긴 증가하는 부분 수열.txt","r")
n=int(input())

num=list(map(int,input().split()))

dp=[0 for _ in range(n)]
#print(dp)


# 자기 자신 보다 작은 숫자들 중 가장 큰 길이를 구하고 그 길이에 +1을 하면 된다.
for i in range(n):
    for j in range(i):
        if num[i]>num[j] and dp[i]<dp[j]:
            dp[i]=dp[j]
    dp[i]+=1
print(max(dp))