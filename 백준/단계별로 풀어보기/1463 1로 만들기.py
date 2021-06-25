import sys
sys.stdin=open('1463 1로 만들기.txt',"r")
T=int(input())

for tc in range(T):
    n=int(input())
    dp=[0]*1000001
    dp[1]=0
    dp[2]=1
    dp[3]=1

    if n>3:
        for i in range(4,n+1):
            if i%2==0 and i%3==0:
                dp[i]=min(dp[i-1],dp[i//2],dp[i//3])+1
            elif i%2==0:
                dp[i]=min(dp[i-1], dp[i//2])+1
            elif i%3==0:
                dp[i]=min(dp[i-1],dp[i//3])+1
            else:
                dp[i]=dp[i-1]+1
        print(dp[n])
    else:
        print(dp[n])