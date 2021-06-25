import sys
sys.stdin=open('2805 나무 자르기.txt',"r")

#pypy로 통과
N, M = map(int,input().split())
trees=list(map(int,input().split()))
trees.sort()

start=0
end=trees[-1]
ans=0

while start <= end:
    mid = (start + end) // 2
    cnt = 0

    for i in trees:
        if i-mid>0:
            cnt += i - mid

    if cnt >= M:
        start = mid + 1
        if ans< mid:
            ans=mid
    else:
        end = mid - 1

print(ans)

# 이건 파이썬도 통과// 도대체 차이가 뭐냐?! 어어어??
N, M = map(int, input().split())
trees = list(map(int, input().split()))
trees.sort()

start = 0
end = trees[-1]
ans = 0

while start <= end:
    mid = (start + end) // 2

    cnt = sum([i - mid if mid < i else 0 for i in trees])

    if cnt >= M:
        start = mid + 1
        if ans < mid:
            ans = mid
    elif cnt < M:
        end = mid - 1

print(ans)
