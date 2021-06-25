import sys
sys.stdin=open("2740 행렬 곱셈.txt","r")

N, M = map(int,input().split())
A=[list(map(int,input().split())) for _ in range(N)]

M, K = map(int,input().split())
B=[list(map(int,input().split())) for _ in range(M)]

#2번 방법
ans=[]

for i in range(N):
    for k in range(K):
        num = 0
        for j in range(M):
            num+=A[i][j]*B[j][k]
        ans.append(num)
    # 1번 방법
    #     print(num, end=" ")
    # print()

cnt=0
while ans:
    if cnt<2:
        print(ans.pop(0), end=" ")
        cnt+=1
    else:
        print(ans.pop(0))
        cnt+=1

    if cnt==3:
        cnt=0
