import sys
sys.stdin=open("11651 좌표 정렬하기2.txt","r")

ipt = sys.stdin.readline
N=int(ipt())
coordinate=[]

for _ in range(N):
    A, B = map(int,ipt().split())
    coordinate.append((A, B))
ans=sorted(coordinate, key=lambda x:(x[1],x[0]))

for i in ans:
    x, y = i[0],i[1]
    print(x,y)