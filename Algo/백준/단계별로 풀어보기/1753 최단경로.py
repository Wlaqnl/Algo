import sys, heapq
sys.stdin=open("1753 최단경로.txt","r", encoding='utf-8')
input = sys.stdin.readline

def dijkstra(v, start, g):
    dist=[INF]*(v+1)
    dist[start]=0
    q=[]
    heapq.heappush(q,[0,start])

    while q:
        cost, loc=heapq.heappop(q)
        for l, c in g[loc]:
            c+=cost
            if c<dist[l]:
                dist[l]=c
                heapq.heappush(q,[c,l])
    return dist[1:]

V, E = map(int,input().split())
K=int(input())
g=[[] for i in range(V+1)]
INF=1e9

for i in range(E):
    u, v, w = map(int,input().split())
    g[u].append([v,w])

for x in dijkstra(V,K,g):
    print(x if x!=INF else "INF")