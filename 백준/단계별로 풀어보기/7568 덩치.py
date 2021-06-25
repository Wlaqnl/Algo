import sys
sys.stdin=open("7568 덩치.txt","r")

n=int(input())
build=[]

for _ in range(n):
    weight, height=map(int,input().split())
    build.append((weight, height))


for i in range(n):
    cnt=0
    for j in range(n):
        if i==j:
            continue
        if build[i][0]<build[j][0] and build[i][1]<build[j][1]:
            cnt+=1
    rank=cnt+1
    print(rank, end=' ')

