from itertools import combinations
import sys
sys.stdin=open("15650 N과 M(2).txt","r")
T=int(input())

def f(n,m,k,l):
    if(n == k):
        print(*res)
        return
    else:
        for i in range(m):
            if(visited[i]==0 and l<arr[i]):
                visited[i] = 1
                l = arr[i]
                res[n] = arr[i]
                f(n+1,m,k,l)
                visited[i] = 0

for tc in range(T):
    # 조합으로 풀기
    # N, M = map(int, input().split())
    # num = []
    #
    # for i in range(1, N + 1):
    #     num.append(i)
    #
    # ans = list(combinations(num, M))
    #
    # for j in ans:
    #     print(' '.join(map(str, j)))

    # 백트래킹으로 풀기
    n, m = map(int, input().split())

    arr = [i+1 for i in range(n)]
    visited = [0 for i in range(n)]
    res = [0] * m
    f(0, n, m, 0)
