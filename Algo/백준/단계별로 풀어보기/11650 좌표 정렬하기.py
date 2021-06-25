import sys
sys.stdin=open("11650 좌표 정렬하기.txt","r")

N=int(input())
coordinate=[]

for _ in range(N):
    A, B = map(int,input().split())
    coordinate.append((A, B))
ans=sorted(coordinate, key=lambda x:(x[0],x[1]))

for i in ans:
    x, y = i[0],i[1]
    print(x,y)


