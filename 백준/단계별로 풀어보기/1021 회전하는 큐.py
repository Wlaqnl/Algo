from collections import deque
import sys
sys.stdin=open('1021 회전하는 큐.txt',"r")
T=int(input())

#deque.rotate(iter) : iter횟수만큼 deque의 맨 뒷 값을 맨 앞으로 이동
#deque.rotate(-iter) : iter횟수만큼 deque의 맨 앞 값을 맨 뒤로 이동

for tc in range(T):
    N, M = map(int,input().split())
    jimin=deque(list(map(int,input().split())))
    num=deque([i+1 for i in range(N)])
    cnt=0

    while jimin:
        value=jimin.popleft()

        if num[0]==value:
            num.popleft()
        else:
            value_idx=num.index(value)
            #앞으로 옮기는게 유리한 경우
            if value_idx>len(num)//2:
                num.rotate(len(num)-value_idx)
                cnt+=(len(num)-value_idx)
                num.popleft()

            #뒤로 옮기는게 유리한 경우
            else:
                num.rotate(-value_idx)
                cnt+=value_idx
                num.popleft()
    print(cnt)

