import sys
sys.stdin=open("안테나.txt","r")

n=int(input())
data=list(map(int,input().split()))
data.sort()

print(data[(n-1)//2])