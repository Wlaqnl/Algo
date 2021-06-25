from collections import deque
import sys
sys.stdin=open("7569 토마토.txt","r")
T=int(input())

#pypy로 해야 통과됌 ㅜㅜ
for tc in range(T):
    M, N, H = map(int,input().split())
    tomato=[[list(map(int,input().split())) for _ in range(N)] for _ in range(H)]
    visited=[[[0]*M for _ in range(N)] for _ in range(H)]
    q=deque([])
    check=True
    ans=0
    cnt=0

    for i in range(H):
        for j in range(N):
            for k in range(M):
                if tomato[i][j][k]==1:
                    q.append((i,j,k))
                    visited[i][j][k]=1
                elif visited[i][j][k]==-1:
                    cnt+=1

    if len(q)==H*M*N-cnt:
        print(0)
    else:
        dx=[1,-1,0,0,0,0]
        dy=[0,0,1,-1,0,0]
        dz=[0,0,0,0,1,-1]

        while q:
            z,y,x = q.popleft()

            for k in range(6):
                nx=x+dx[k]
                ny=y+dy[k]
                nz=z+dz[k]

                if 0<=nx<M and 0<=ny<N and 0<=nz<H and tomato[nz][ny][nx]==0 and not visited[nz][ny][nx]:
                    tomato[nz][ny][nx]=1
                    visited[nz][ny][nx]=visited[z][y][x]+1
                    q.append((nz,ny,nx))

        for i in range(H):
            for j in range(N):
                if 0 in tomato[i][j]:
                    check=False
                    break
                else:
                    if ans<max(visited[i][j]):
                        ans=max(visited[i][j])

        if check:
            print(ans-1)
        else:
            print(-1)