import sys,heapq,bisect
sys.stdin=open('1655 가운데를 말해요.txt',"r")

#시간 초과
# N=int(input())
# hihi=[]
#
# for _ in range(N):
#     heapq.heappush(hihi,int(sys.stdin.readline()))
#     n=len(hihi)
#     hihi.sort()
#     if n==1:
#         print(hihi[0])
#     elif n%2:
#         print(hihi[n//2])
#     else:
#         print(min(hihi[n//2-1], hihi[n//2]))
#

# 최대힙 최소힙 이용
max_heap = []
min_heap = []

for _ in range(int(input())):
    num = int(sys.stdin.readline())
    if len(max_heap) == len(min_heap):
        heapq.heappush(max_heap, (-num, num))
    else:
        heapq.heappush(min_heap, (num, num))

    if min_heap and max_heap[0][1] > min_heap[0][1]:
        max_value = heapq.heappop(max_heap)[1]
        min_value = heapq.heappop(min_heap)[1]
        heapq.heappush(min_heap, (max_value, max_value))
        heapq.heappush(max_heap, (-min_value, min_value))

    print(max_heap[0][1])

#bisect 이용 - 시간초과
# input = sys.stdin.readline
# n = int(input().rstrip())
# x = []
# answers = []
#
# for _ in range(n):
#     bisect.insort(x, int(input().rstrip()))
#     if(len(x) % 2 == 0):
#         answers.append(x[int(len(x)/2)-1])
#     else:
#         answers.append(x[int(len(x)/2)])
# for a in answers:
#     print(a)

