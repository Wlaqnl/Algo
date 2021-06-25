from math import factorial
import sys
sys.stdin=open("1676 팩토리얼 0의 개수.txt","r")

T=int(input())

for tc in range(T):
    N=int(input())
    num=str(factorial(N))
    n=len(num)
    cnt=0
    #print(num)

    for i in range(n-1,-1,-1):
        if num[i]=='0':
            cnt+=1
        else:
            print(cnt)
            break