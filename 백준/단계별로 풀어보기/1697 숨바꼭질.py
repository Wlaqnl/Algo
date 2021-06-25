from collections import deque
import sys
sys.stdin=open("1697 숨바꼭질.txt","r")

N, K = map(int,input().split())
q=deque([])
q.append((N,1))
check=[False]*100001
check[N]=True

if N==K:
    print(0)
else:
    while q:
        x, cnt=q.popleft()

        if x+1==K:
            break
        elif x-1==K:
            break
        elif x*2==K:
            break
        else:
            if x+1<=100000:
                if check[x+1]==False:
                    q.append((x+1, cnt+1))
                    check[x+1]=True

            if x-1>0:
                if check[x-1]==False:
                    q.append((x-1, cnt+1))
                    check[x-1]=True

            if x*2<=100000:
                if check[x*2]==False:
                    q.append((x * 2,cnt+1))
                    check[x*2]=True

    print(cnt)