from math import gcd
import sys
sys.stdin=open("3036 링.txt","r")

N=int(input())

ring=list(map(int,input().split()))

for i in range(1,N):
    q=gcd(ring[0],ring[i])
    print("{}/{}".format(ring[0]//q,ring[i]//q))