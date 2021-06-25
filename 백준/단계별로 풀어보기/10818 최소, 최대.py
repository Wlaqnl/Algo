import sys
sys.stdin=open("10818 최소, 최대.txt","r")

n=int(input())
num=list(map(int,input().split()))
print(min(num),max(num))