from collections import deque
import sys
sys.stdin=open("5430 AC.txt","r")
T=int(input())

for tc in range(T):
    order=input()
    n=int(input())
    reverse_temp=0
    if n:
        arr=deque(list(map(int,input()[1:-1].split(','))))
    else:
        arr=deque(input()[1:-1])

    temp=True

    for o in order:
        if o=='R':
            if reverse_temp==0:
                reverse_temp=1
            else:
                reverse_temp=0
        else:
            if arr:
                if reverse_temp:
                    arr.pop()
                else:
                    arr.popleft()
            else:
                temp=False
                break

    if temp:
        if reverse_temp:
            arr.reverse()

        print("[", end='')
        for j in range(len(arr)):
            if j == len(arr) - 1:
                print(arr[j], end='')
            else:
                print(arr[j], end=',')
        print(']')

    else:
        print('error')

