from collections import deque
import sys
sys.stdin=open("1260 DFS와 BFS.txt","r")
T=int(input())

def DFS(graph,v,visited, arr):
    visited[v]=True
    arr.append(v)

    for i in graph[v]:
        if not visited[i]:
            DFS(graph,i,visited,arr)


def BFS(graph, v, visited, arr):
    queue=deque([v])
    visited[v]=True

    while queue:
        v=queue.popleft()
        arr.append(v)
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i]=True


for tc in range(T):
    N, M, V = map(int,input().split())
    graph=[[] for _ in range(N+1)]
    dot=[list(map(int,input().split())) for _ in range(M)]
    visited=[False]*(N+1)
    ans1=[]
    ans2=[]

    for x, y in dot:
        graph[x].append(y)
        graph[y].append(x)

    for i in graph:
        i.sort()

    DFS(graph, V, visited, ans1)
    visited=[False]*(N+1)
    BFS(graph, V, visited, ans2)

    print(*ans1)
    print(*ans2)