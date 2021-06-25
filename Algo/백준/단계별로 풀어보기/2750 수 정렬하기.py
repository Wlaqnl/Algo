import sys
sys.stdin=open('2750 수 정렬하기.txt',"r")

N=int(input())
num=[]

for _ in range(N):
    num.append(int(input()))
num.sort()

for n in num:
    print(n)