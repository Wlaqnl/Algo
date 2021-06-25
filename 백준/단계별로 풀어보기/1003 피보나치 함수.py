import sys
sys.stdin=open("1003 피보나치 함수.txt","r")
N=int(input())

for n in range(N):
    num=int(input())
    zero=1
    one=0
    temp=0

    for _ in range(num):
        temp=one
        one=one+zero
        zero=temp
    print(zero,one)