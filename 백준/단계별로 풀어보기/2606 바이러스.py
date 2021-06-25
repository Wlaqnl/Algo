import sys
sys.stdin=open("2606 바이러스.txt","r")

def DFS(graph, v, visited):
    global cnt

    visited[v]=True
    cnt+=1

    for i in graph[v]:
        if not visited[i]:
            DFS(graph, i, visited)

N=int(input())
M=int(input())
computer=[list(map(int,input().split())) for _ in range(M)]
virus=[[] for _ in range(N+1)]
visited=[False]*(N+1)
cnt=0

for a, b in computer:
    virus[a].append(b)
    virus[b].append(a)

DFS(virus, 1, visited)
print(cnt-1)

