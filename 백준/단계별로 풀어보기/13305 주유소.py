import sys
sys.stdin=open('13305 주유소.txt',"r")
T=int(input())

# 시간초과
# for tc in range(T):
#     N=int(input())
#     dist=list(map(int,input().split()))
#     oil=list(map(int,input().split()))
#
#     minV=oil[0]*sum(dist)
#     save=0
#     before=[0]
#
#     for i in range(1,N):
#         price=oil[save]*sum(dist[save:i])
#         if minV>oil[i]*sum(dist[i:])+sum(before)+price:
#             minV=oil[i]*sum(dist[i:])+sum(before)+price
#             save=i
#             before.append(price)
#     print(minV)

# oil가격을 매번 비교하여 최솟값을 저장해서 사용한다.
for tc in range(T):
    N=int(input())
    dist=list(map(int,input().split()))
    oil=list(map(int,input().split()))
    total=0
    minV=1e9

    for i in range(N-1):
        if i==0:
            total+=dist[i]*oil[i]
            minV=min(minV,oil[i])
        else:
            minV=min(minV,oil[i])
            total+=minV*dist[i]
    print(total)