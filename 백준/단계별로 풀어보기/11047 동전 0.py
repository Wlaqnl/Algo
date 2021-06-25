import sys
sys.stdin=open("11047 동전 0.txt","r")
T=int(input())

for tc in range(T):
    N, K = map(int,input().split())
    value=[]
    cnt=0
    i=0

    for n in range(N):
        value.append(int(input()))
    value.sort(reverse=True)

    while K:
        for v in range(i,len(value)):
            if value[v]>K:
                continue
            else:
                q=K//value[v]
                K-=value[v]*q
                cnt+=q
                i=v
                break
    print(cnt)