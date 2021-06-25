from collections import deque
import sys
sys.stdin=open("2178 미로 탐색.txt","r")
T=int(input())

dx=[1,-1,0,0]
dy=[0,0,1,-1]

def BFS(x, y):
    #deque는 기본정의 해놓고 append해서 사용해야함
    queue=deque()
    queue.append((x,y))

    while queue:
        i,j=queue.popleft()

        for k in range(4):
            ni=i+dx[k]
            nj=j+dy[k]

            if 0<=ni<N and 0<=nj<M and not check[ni][nj] and miro[ni][nj]:
                check[ni][nj] = check[i][j] + 1
                if ni == N - 1 and nj == M - 1:
                    break
                else:
                    queue.append((ni,nj))


    return check[N-1][M-1]

for tc in range(T):
    N, M = map(int,input().split())
    miro=[list(map(int, input())) for _ in range(N)]
    check=[[0]*M for _ in range(N)]
    check[0][0]=1

    print(BFS(0,0))




