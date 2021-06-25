import sys
sys.stdin=open("1932 정수 삼각형.txt","r")
N=int(input())

triangle=[]
for _ in range(N):
    triangle.append(list(map(int,input().split())))
#print(triangle)

if N>=2:
    for i in range(1,N):
        for j in range(i+1):
            if j==i:
                triangle[i][j] += triangle[i - 1][j - 1]
            elif j==0:
                triangle[i][j]+=triangle[i-1][j]
            else:
                triangle[i][j] += max(triangle[i - 1][j], triangle[i - 1][j - 1])

    print(max(triangle[N-1]))

else:
    print(triangle[0][0])
