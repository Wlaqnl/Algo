from itertools import combinations
import sys
sys.stdin=open("15651 N과 M(3).txt","r")
T=int(input())

def f(n,m,k):
    if(n==k):
        print(*res)
        return
    else:
        for i in range(m):
            visited[i]=1
            res[n]=arr[i]
            f(n+1,m,k)
            visited[i]=0

for tc in range(T):
    N, M = map(int,input().split())
    arr = [i+1 for i in range(N)]
    visited=[0 for i in range(N)]
    res=[0]*M
    f(0,N,M)