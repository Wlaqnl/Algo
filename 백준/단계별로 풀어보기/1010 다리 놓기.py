from math import factorial
import sys
sys.stdin=open("1010 다리 놓기.txt","r")

#mCn
n=int(input())

for tc in range(n):
    N, M = map(int,input().split())
    print(factorial(M)//(factorial(M-N)*factorial(N)))