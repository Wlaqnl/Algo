import sys
sys.stdin=open("2667 단지번호붙이기.txt","r")

def DFS(x, y, visited):
    global cnt

    for k in range(4):
        nx=x+dx[k]
        ny=y+dy[k]

        if 0<=nx<N and 0<=ny<N and map[nx][ny]==1:
            if not visited[nx][ny]:
                cnt+=1
                visited[nx][ny]=True
                DFS(nx, ny, visited)


N=int(input())
map=[list(map(int,input())) for _ in range(N)]
visited=[[False]*N for _ in range(N)]
dansi=[]

dx=[1,-1,0,0]
dy=[0,0,1,-1]

for i in range(N):
    for j in range(N):
        if not visited[i][j] and map[i][j]:
            cnt = 1
            visited[i][j]=True
            DFS(i, j, visited)
            if cnt:
                dansi.append(cnt)

dansi.sort()
print(len(dansi))

for d in dansi:
    print(d)