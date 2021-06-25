import sys,heapq
sys.stdin=open("11286 절댓값 힙.txt","r")

N=int(input())
hihi=[]

for _ in range(N):
    x=int(sys.stdin.readline())
    if x:
        heapq.heappush(hihi,(abs(x), x))
    else:
        if hihi:
            a, b=heapq.heappop(hihi)
            print(b)
        else:
            print(0)