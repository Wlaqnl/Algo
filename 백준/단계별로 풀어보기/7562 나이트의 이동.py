from collections import deque
import sys
sys.stdin=open("7562 나이트의 이동.txt", "r")
T=int(input())

for tc in range(T):
    L=int(input())
    sx,sy=map(int,input().split())
    fx,fy=map(int,input().split())
    visited=[[0]*L for _ in range(L)]
    visited[sy][sx]=1

    #나이트 이동
    dx=[-1,-2,-2,-1,1,2,2,1]
    dy=[2,1,-1,-2,-2,-1,1,2]

    q=deque([(sx,sy)])

    while q:
        x, y = q.popleft()

        if x==fx and y==fy:
            print(visited[y][x]-1)
            break

        for k in range(8):
            nx=x+dx[k]
            ny=y+dy[k]

            if 0<=nx<L and 0<=ny<L and visited[ny][nx]==0:
                visited[ny][nx] = visited[y][x] + 1
                q.append((nx, ny))

    print(visited)

