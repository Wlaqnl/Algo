import sys
sys.stdin=open("1712 손익분기점.txt","r")
T=int(input())

for tc in range(T):
    A, B, C = map(int,input().split())
    cnt=1
    if B>=C:
        print(-1)
    else:
        value=int(A/(C-B))+1
        print(value)

