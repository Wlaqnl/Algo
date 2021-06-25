import sys
sys.stdin=open("2739 구구단.txt","r")

n=int(input())

for i in range(1,10):
    print(n, "*", i, "=", n*i)
    