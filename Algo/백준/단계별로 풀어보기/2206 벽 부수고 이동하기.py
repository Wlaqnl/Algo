from collections import deque
import sys
sys.stdin=open("2206 벽 부수고 이동하기.txt","r", encoding='utf-8')
T=int(input())

for tc in range(T):
    N, M = map(int,input().split())
    #map 이름 겹치면 안돼~~!!
    mapp=[list(map(int,input())) for _ in range(N)]
    visited=[[[0]*M for _ in range(N)] for _ in range(2)]

    dx=[1,-1,0,0]
    dy=[0,0,1,-1]

    q=deque([])

    if N==1 and M==1 and mapp[0][0]==0:
        print(1)

    else:
        q.append((0, 0, 0))
        visited[0][0][0] = 1

        flag=0
        while q:
            x, y, z = q.popleft()

            for k in range(4):
                nx=x+dx[k]
                ny=y+dy[k]

                if 0<=nx<M and 0<=ny<N and visited[z][ny][nx]==0:

                    #벽을 안 만났을 때
                    if mapp[ny][nx]==0:
                        visited[z][ny][nx]=visited[z][y][x]+1
                        q.append((nx,ny,z))

                    #벽을 만났는데 아직 벽을 안 뚫었을 때
                    elif mapp[ny][nx]==1 and z==0:
                        visited[1][ny][nx]=visited[0][y][x]+1
                        q.append((nx,ny,1))

                    #도착
                    if ny==N-1 and nx==M-1:
                        print(visited[z][ny][nx])
                        flag=1
                        break

            if flag==1:
                break

        if flag==0:
            print(-1)


