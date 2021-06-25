import sys
sys.stdin=open("10989 수 정렬하기3.txt","r")

ipt=sys.stdin.readline
count=[0]*10001
for _ in range(int(ipt())):
    count[int(ipt())]+=1

n=0
for i in count:
    if i:
        for j in range(i):
            print(n)
    n+=1
