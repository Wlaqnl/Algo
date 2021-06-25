import sys
sys.stdin=open('1037 약수.txt',"r")

N=int(input())
divisor=list(map(int,input().split()))
divisor.sort()

if N%2:
    print(divisor[len(divisor)//2]**2)
else:
    print(divisor[0] * divisor[-1])