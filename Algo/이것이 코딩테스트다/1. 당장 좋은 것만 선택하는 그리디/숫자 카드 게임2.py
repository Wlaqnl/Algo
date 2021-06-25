import sys
sys.stdin=open("숫자 카드 게임.txt", "r")
T=int(input())

for tc in range(T):
    N, M = map(int,input().split())
    result=0

    for i in range(N):
        data = list(map(int,input().split()))
        min_value=10001
        for a in data:
            min_value =min(min_value, a)
        result=max(result, min_value)

print(result)