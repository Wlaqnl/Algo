from collections import deque
import sys
sys.stdin=open("7576 토마토.txt","r")
T=int(input())

for tc in range(T):
    M, N = map(int,input().split())
    tomato=[list(map(int,input().split())) for _ in range(N)]
    check=True
    visited = [[0] * M for _ in range(N)]
    q=deque([])
    ans=0
    cnt=0

    for i in range(N):
        for j in range(M):
            if tomato[i][j]==1:
                q.append((i,j))
                visited[i][j]=1
            elif tomato[i][j]==-1:
                cnt+=1

    if len(q)==M*N-cnt:
        print(0)
    else:
        dx=[1,-1,0,0]
        dy=[0,0,1,-1]

        while q:
            y, x = q.popleft()

            for k in range(4):
                nx=x+dx[k]
                ny=y+dy[k]

                if 0<=nx<M and 0<=ny<N and tomato[ny][nx]==0 and not visited[ny][nx]:
                    tomato[ny][nx]=1
                    visited[ny][nx]=visited[y][x]+1
                    q.append((ny,nx))

        for i in range(N):
            if 0 in tomato[i]:
                check=False
                break
            else:
                if ans<max(visited[i]):
                    ans=max(visited[i])
        if check:
            print(ans-1)
        else:
            print(-1)

