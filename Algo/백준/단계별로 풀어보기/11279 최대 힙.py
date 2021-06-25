import heapq
import sys
sys.stdin=open("11279 최대 힙.txt")

#sys.stdin.readline() 안하면 시간초과뜸 ㅋㅋㅋ

N=int(input())
hehe=[]

for _ in range(N):
    x=int(sys.stdin.readline())
    if x:
        heapq.heappush(hehe, -x)
    else:
        if hehe:
            print(heapq.heappop(hehe)*(-1))
        else:
            print(0)

