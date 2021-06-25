import sys
sys.stdin=open("1546 평균.txt","r")

T=int(input())
for tc in range(T):
    n=int(input())
    num=list(map(int,input().split()))
    average=0

    for i in range(n):
        average+=num[i]/max(num)*100

    print(average/n)

