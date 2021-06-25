import sys
sys.stdin=open("효율적인 화폐 구성.txt","r")
T=int(input())

for tc in range(T):
    N, M = map(int,input().split())
    array=[]
    for i in range(N):
        array.append(int(input()))

    d=[10001]*(M+1)

    d[0]=0
    for i in range(N):
        for j in range(array[i], M+1):
            if d[j-array[i]]!=10001:
                d[j]=min(d[j],d[j-array[i]]+1)

    if d[M]==10001:
        print(-1)
    else:
        print(d[M])