import sys
sys.stdin=open("15651 N과 M(3).txt","r")
T=int(input())

def f(n,m,k,l):
    if(n == k):
        print(*res)
        return
    else:
        for i in range(m):
            if(arr[i] >= l):
                visited[i] = 1
                l = arr[i]
                res[n] = arr[i]
                f(n+1,m,k,l)
                visited[i] = 0

for tc in range(T):
    n, m = map(int, input().split())
    arr = [i+1 for i in range(n)]
    visited = [0 for i in range(n)]
    res = [0] * m
    f(0,n,m,0)