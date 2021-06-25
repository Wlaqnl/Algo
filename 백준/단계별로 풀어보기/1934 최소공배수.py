from math import gcd
import sys
sys.stdin=open("1934 최소공배수.txt","r")
T=int(input())

def lcd(a,b):
    return a*b//gcd(a,b)

for tc in range(T):
    A, B = map(int, input().split())
    print(lcd(A,B))

