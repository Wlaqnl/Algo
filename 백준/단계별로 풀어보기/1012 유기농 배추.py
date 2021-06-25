import sys
sys.stdin=open("1012 유기농 배추.txt","r")
sys.setrecursionlimit(3000)
T=int(input())

def gogosing(x, y):
    for k in range(4):
        nx=x+dx[k]
        ny=y+dy[k]

        if 0<=nx<N and 0<=ny<M and not visited[nx][ny] and cabbage[nx][ny]:
            visited[nx][ny]=True
            gogosing(nx,ny)

for tc in range(T):
    te=int(input())

    dx=[1,-1,0,0]
    dy=[0,0,1,-1]

    for t in range(te):
        M, N, K = map(int,input().split())
        cabbage=[[0]*M for _ in range(N)]
        visited=[[False]*M for _ in range(N)]
        earthworm=0

        for _ in range(K):
            x, y = map(int,input().split())
            cabbage[y][x]=1

        for i in range(N):
            for j in range(M):
                if not visited[i][j] and cabbage[i][j]:
                    earthworm+=1
                    gogosing(i,j)

        print(earthworm)
