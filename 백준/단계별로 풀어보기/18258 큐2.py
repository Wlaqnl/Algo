from collections import deque
import sys
sys.stdin=open("18258 큐2.txt","r")
N=int(sys.stdin.readline())

dq=deque([])

for _ in range(N):
    order=sys.stdin.readline().split()
    #print(order)

    if 'push' in order:
        dq.append(order[1])
    else:
        if 'pop' in order:
            if dq:
                print(dq.popleft())
            else:
                print(-1)
        elif 'size' in order:
            print(len(dq))
        elif 'empty' in order:
            if dq:
                print(0)
            else:
                print(1)
        elif 'front' in order:
            if dq:
                print(dq[0])
            else:
                print(-1)
        else:
            if dq:
                print(dq[-1])
            else:
                print(-1)