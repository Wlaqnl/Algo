import sys
sys.stdin=open("1149 RGB거리.txt","r")

# 시간 초과 ㅠㅠ
# def paint(arr, k, money):
#     global minV
#
#     if k==N+1:
#         if minV>money:
#             minV=money
#         return
#
#
#     for i in range(1,4):
#         if k<N:
#             if arr[k-1]!=i and arr[k+1]!=i:
#                 arr[k]=i
#                 paint(arr,k+1,money+color[k][i])
#                 arr[k]=0
#         else:
#             if arr[k-1]!=i:
#                 arr[k] = i
#                 paint(arr, k + 1, money + color[k][i])
#                 arr[k] = 0
#
# N=int(input())
#
# color=[[0]*4]
#
# for i in range(N):
#     color.append([0]+list(map(int,input().split())))
#
# house=[0]*(N+1)
# minV=1e9
# paint(house,1,0)
# print(minV)

n=int(input())
rgb_pay = [[0] * 3 for i in range(n)]

for i in range(n):
    # 각 색별 페인트 비용
    rgb_pay[i][0], rgb_pay[i][1], rgb_pay[i][2] = map(int, input().split())

# 이번에 빨강,초록,파랑을 골랐을때의 최솟값이 들어간다.0=빨강 1=초록 2=파랑
rgb_sum = [[0] * 3 for i in range(n)]

for i in range(n):
    if i == 0:
        rgb_sum[i] = rgb_pay[i]

    else:
        # 이번에 빨강을 고를때 최솟값(파랑,초록 둘중 작은거)
        # 이번에 초록을 고를때 이전값들중에서 최솟값(빨강,파랑)
        # 이번에 파랑을 고를때 이전값들중에서 최솟값(빨강,초록)
        rgb_sum[i][0] = rgb_pay[i][0] + min(rgb_sum[i - 1][1], rgb_sum[i - 1][2])
        rgb_sum[i][1] = rgb_pay[i][1] + min(rgb_sum[i - 1][0], rgb_sum[i - 1][2])
        rgb_sum[i][2] = rgb_pay[i][2] + min(rgb_sum[i - 1][0], rgb_sum[i - 1][1])

print(min(rgb_sum[n - 1]))  # 최종적으로 빨강,파랑,초록 을 골랐을때 최솟값
