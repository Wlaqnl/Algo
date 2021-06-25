import sys
import heapq
sys.stdin=open('1927 최소 힙.txt','r')

N=int(input())
hihi=[]

for _ in range(N):
    x=int(sys.stdin.readline())
    if x:
        heapq.heappush(hihi,x)
    else:
        if hihi:
            print(heapq.heappop(hihi))
        else:
            print(0)