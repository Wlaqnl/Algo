from collections import deque
import sys
sys.stdin=open("11866 요세푸스 문제0.txt","r")

N, K = map(int,input().split())

dq=deque([i+1 for i in range(N)])
#print(dq)

print('<', end='')

while dq:
    for i in range(K - 1):
        dq.append(dq[0])
        dq.popleft()
    print(dq.popleft(), end='')
    if dq:
        print(', ', end='')
print('>')
