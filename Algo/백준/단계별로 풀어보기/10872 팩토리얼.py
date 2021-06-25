import sys
sys.stdin=open("10872 팩토리얼.txt","r")
T=int(input())

def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)

for tc in range(T):
    N=int(input())
    print(factorial(N))