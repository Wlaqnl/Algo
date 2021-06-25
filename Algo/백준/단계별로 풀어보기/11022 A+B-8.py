import sys
sys.stdin=open("11022 A+B-8.txt","r")
T=int(input())

for tc in range(T):
    a, b = map(int,input().split())
    print("Case #{}: {} + {} = {}".format(tc+1, a, b, a+b))