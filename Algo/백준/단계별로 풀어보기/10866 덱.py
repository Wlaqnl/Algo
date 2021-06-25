from collections import deque
import sys
sys.stdin=open("10866 덱.txt","r")
T=int(input())

for tc in range(T):
    N = int(input())
    dq = deque([])

    for _ in range(N):
        order = sys.stdin.readline().split()

        if 'push_front' in order:
            dq.appendleft(order[1])
        elif 'push_back' in order:
            dq.append(order[1])
        elif 'pop_front' in order:
            if dq:
                print(dq.popleft())
            else:
                print(-1)
        elif 'pop_back' in order:
            if dq:
                print(dq.pop())
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