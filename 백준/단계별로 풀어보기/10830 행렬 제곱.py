import sys
sys.stdin=open("10830 행렬 제곱.txt","r")
T=int(input())

def matrixMul(num):
    global N, matrix
    if num==1:
        for i in range(N):
            for j in range(N):
                matrix[i][j]%=1000
        return matrix
    elif num%2==1:
        tmp=[[0]*N for _ in range(N)]
        C=matrixMul(num-1)
        for i in range(N):
            for j in range(N):
                for k in range(N):
                    tmp[i][j]+=C[i][k]*matrix[k][j]
                tmp[i][j]%=1000
        return tmp
    else:
        tmp = [[0] * N for _ in range(N)]
        C = matrixMul(num//2)
        for i in range(N):
            for j in range(N):
                for k in range(N):
                    tmp[i][j]+=C[i][k]*C[k][j]
                tmp[i][j]%=1000
        return tmp

for tc in range(T):
    N, B = map(int,input().split())

    matrix=[list(map(int,input().split())) for _ in range(N)]

    res=matrixMul(B)

    for i in range(N):
        for j in range(N):
            print(res[i][j], end=" ")
        print()