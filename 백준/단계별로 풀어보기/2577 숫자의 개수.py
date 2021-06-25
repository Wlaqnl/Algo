import sys
sys.stdin=open("2577 숫자의 개수.txt","r")

A=int(input())
B=int(input())
C=int(input())

num=A*B*C

check=[0]*10

while num>10:
    check[num%10]+=1
    num=num//10
check[num]+=1

for i in check:
    print(i)
