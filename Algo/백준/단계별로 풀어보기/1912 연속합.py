import sys
sys.stdin=open("1912 연속합.txt","r")
T=int(input())

for tc in range(T):
    n=int(input())
    num=list(map(int,input().split()))
    plus=[num[0]]

    for i in range(len(num)-1):
        plus.append(max(plus[i]+num[i+1],num[i+1]))
    print(max(plus))