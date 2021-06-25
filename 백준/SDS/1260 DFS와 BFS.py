import sys
sys.stdin=open("1260 DFS와 BFS.txt","r")
T=int(input())


def DFS(start, arr, graph):
    if sum(arr) == N:
        return ans_d

    for i in graph[start]:
        if arr[i] == 0:
            ans_d.append(i)
            arr[i] = 1
            DFS(i, arr, graph)


def BFS(start, arr, graph):
    q = [start]

    while q:
        v = q.pop(0)
        if sum(arr) == N:
            return ans_b

        for i in graph[v]:
            if arr[i] == 0:
                ans_b.append(i)
                q.append(i)
                arr[i] = 1

for tc in range(T):
    N, M, K = map(int, input().split())

    graph = [[] for _ in range(N + 1)]

    visited_d = [0] * (N + 1)
    visited_d[K] = 1
    ans_d = [K]

    visited_b = [0] * (N + 1)
    visited_b[K] = 1
    ans_b = [K]

    for _ in range(M):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    for g in graph:
        g.sort()

    DFS(K, visited_d, graph)
    BFS(K, visited_b, graph)

    print(' '.join(map(str, ans_d)))
    print(' '.join(map(str, ans_b)))