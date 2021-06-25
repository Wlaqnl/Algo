from math import gcd
import sys
sys.stdin=open("2609 최대공약수와 최소공배수.txt","r")

A, B = map(int,input().split())
def lcm(x,y):
    return x*y//gcd(x,y)
print(gcd(A,B))
print(lcm(A,B))
