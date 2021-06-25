import sys
sys.stdin=open("7579 앱.txt","r")

#https://m.blog.naver.com/PostView.nhn?blogId=hands731&logNo=221810289506&proxyReferer=https:%2F%2Fwww.google.com%2F
N, M=map(int,input().split())
memory=list(map(int,input().split()))
cost=list(map(int,input().split()))
app=[]
dp=[0]*(sum(cost)+1)

for i in range(N):
    app.append((cost[i],memory[i]))
app=sorted(app, key=lambda x: (x[0],-x[1]))
#print(app)

#중첩을 막기 위해 거꾸로 하기
for a, b in app:
    for j in range(sum(cost),a-1,-1):
        dp[j]=max(dp[j],dp[j-a]+b)

#print(dp)

for j in range(sum(cost)+1):
    if dp[j]>=M:
        print(j)
        break
