import sys
sys.stdin=open("1520 내리막 길.txt","r")
sys.setrecursionlimit(10000)

# def find(x, y, now):
#     global cnt
#
#     if y==M-1 and x==N-1:
#         return 1
#
#     if dp[y][x]==-1:
#         dp[y][x]=0
#         for k in range(4):
#             nx=x+dx[k]
#             ny=y+dy[k]
#             if 0<=nx<N and 0<=ny<M and road[ny][nx]<now:
#                 dp[y][x]+=find(nx, ny, road[ny][nx])
#
#     return dp[y][x]
#
#
# M, N = map(int,input().split())
# road=[list(map(int,input().split())) for _ in range(M)]
#
# #동서남북
# dx=[1,-1,0,0]
# dy=[0,0,1,-1]
# dp=[[-1]*N for _ in range(M)]
#
# print(find(0, 0, road[0][0]))

def dfs(x, y):
    if x == n-1 and y == m-1:
        return 1
    rtn = 0
    for d in range(4):
        i, j = x + dx[d], y + dy[d]
        if 0 <= i < n and 0 <= j < m and mountain[i][j] < mountain[x][y]:
            if visited[i][j] >= 0:
                rtn += visited[i][j]
            else:
                rtn += dfs(i, j)
    visited[x][y] = rtn
    return rtn

n, m = map(int, input().split())
mountain = [list(map(int, input().split())) for _ in range(n)]
visited = [[-1] * m for _ in range(n)]
visited[0][0] = 0
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
print(dfs(0, 0))
print(visited)
