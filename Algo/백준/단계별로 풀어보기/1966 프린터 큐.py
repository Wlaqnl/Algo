from collections import deque
import sys
sys.stdin=open("1966 프린터 큐.txt","r")
T=int(input())

for tc in range(T):
    N, M = map(int,input().split())
    imp=deque(list(map(int,input().split())))
    order=deque(list(i for i in range(N)))
    ans=0

    if N==1:
        print(1)
    else:
        while True:
            value=imp.popleft()
            turn=order.popleft()
            #imp, order 존재해야 값을 비교할 수 있음!
            if imp and order:
                if value<max(imp):
                    imp.append(value)
                    order.append(turn)
                else:
                    if turn==M:
                        ans+=1
                        print(ans)
                        break
                    else:
                        ans+=1
            else:
                ans+=1
                print(ans)
                break

