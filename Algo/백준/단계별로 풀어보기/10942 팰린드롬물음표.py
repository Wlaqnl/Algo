import sys
sys.stdin=open("10942 팰린드롬물음표.txt","r")

N=int(input())
board=list(map(int,input().split()))
dp=[[0]* (N+1) for _ in range(N+1)]

i=N
while i>0:
    j=N
    while j>=i:
        if i==j:
            dp[i][j]=1
        elif j-i==1 and board[i-1]==board[j-1]:
            dp[i][j]=1
        elif board[i-1]==board[j-1] and dp[i+1][j-1]==1:
            dp[i][j]=1
        j-=1
    i-=1
M=int(input())
for _ in range(M):
    s,e = [int(x) for x in sys.stdin.readline().split()]
    print(dp[s][e])



