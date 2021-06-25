from itertools import permutations
import sys
sys.stdin=open("15649 N과 M(1).txt","r")
T=int(input())

def f(n,m,k):
    if(n == k):
        print(*res)
        return
    else:
        for i in range(m):
            if(visited[i] == 0):
                visited[i] = 1
                res[n] = arr[i]
                f(n+1,m,k)
                visited[i] = 0


for tc in range(T):
    #순열로 풀기
    # N, M = map(int,input().split())
    # num=[]
    #
    # for i in range(1, N+1):
    #     num.append(i)
    #
    # ans=list(permutations(num,M))
    #
    # for j in ans:
    #     print(' '.join(map(str,j)))

    #백트래킹으로 풀기
    n, m = map(int, input().split())

    arr = [i+1 for i in range(n)]
    res = [0] * m
    visited = [0 for i in range(n)]
    f(0, n, m)

