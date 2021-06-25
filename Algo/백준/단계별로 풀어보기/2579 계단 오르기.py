import sys
sys.stdin=open("2579 계단 오르기.txt","r")

# 완전탐색은 시간초과
# def step(position, score, method):
#     global maxV
#
#     if position==n:
#         if maxV<score:
#             maxV=score
#         return
#
#     if method==1:
#         if position==1:
#             if position+2<=n:
#                 step(position + 1, score + stairs[position+1], 1)
#                 step(position + 2, score + stairs[position+2], 2)
#             else:
#                 step(position + 1, score + stairs[position+1], 1)
#
#         else:
#             if position+2<=n:
#                 # check[position+2]=1
#                 step(position + 2,score + stairs[position+2], 2)
#     else:
#         if position+2<=n:
#             step(position + 1, score + stairs[position+1], 1)
#             step(position + 2, score + stairs[position+2], 2)
#         else:
#             step(position + 1, score + stairs[position+1], 1)
#
# n=int(input())
# stairs=[0]
#
# for _ in range(n):
#     stairs.append(int(input()))
#
# maxV=0
# step(0,0,1)
# if n>=2:
#     step(0,0,2)
# print(maxV)

# 동적 프로그래밍
n = int(input())
s = [0 for i in range(301)]
dp = [0 for i in range(301)]
for i in range(n):
    s[i] = int(input())
dp[0] = s[0]
dp[1] = s[0] + s[1]
dp[2] = max(s[1] + s[2], s[0] + s[2])
for i in range(3, n):
    dp[i] = max(dp[i - 3] + s[i - 1] + s[i], dp[i - 2] + s[i])
print(dp[n - 1])


