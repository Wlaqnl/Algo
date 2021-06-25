from collections import deque
import sys
sys.stdin=open("1707 이분 그래프.txt","r")

input=sys.stdin.readline
T=int(input())

def bfs(start):
    visited[start]=1
    q=deque()
    q.append(start)

    while q:
        a=q.popleft()
        for i in graph[a]:
            if visited[i]==0:
                visited[i]=-visited[a]
                q.append(i)
            else:
                if visited[i]==visited[a]:
                    return False
    return True

for tc in range(T):
    V, E = map(int,input().split())
    gansun=[list(map(int,input().split())) for _ in range(E)]
    graph=[[] for _ in range(V+1)]
    visited=[0]*(V+1)
    isTrue=True

    for i in range(E):
        graph[gansun[i][0]].append(gansun[i][1])
        graph[gansun[i][1]].append(gansun[i][0])

    for j in range(1, V+1):
        if visited[j]==0:
            if not bfs(j):
                isTrue=False
                break

    print("YES" if isTrue else "NO")