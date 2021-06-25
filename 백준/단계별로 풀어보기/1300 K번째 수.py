import sys
sys.stdin=open("1300 K번째 수.txt","r")

N=int(input())
K=int(input())

left = 1
right = K
ans = 0

while left <= right:
    count = 0
    mid = (left + right) // 2

    for i in range(1, N + 1):
        count += min(mid // i, N)
    if (count < K):
        left = mid + 1
    else:
        ans = mid
        right = mid - 1
print(ans)