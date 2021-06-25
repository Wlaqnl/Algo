import sys
sys.stdin=open("3052 나머지.txt","r")
T=int(input())

for tc in range(T):
    num=[0]*42
    for _ in range(10):
        num[int(input())%42]+=1
    print(42-num.count(0))