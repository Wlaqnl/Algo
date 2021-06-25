import sys
sys.stdin=open("10828 스택.txt","r")
T=int(input())

for tc in range(T):
    N=int(input())
    order=[]
    stack=[]

    for _ in range(N):
        order.append(input().split())

    for i in order:
        if 'push' in i:
            stack.append(i[1])
        else:
            if 'pop' in i:
                if stack:
                    print(stack.pop())
                else:
                    print(-1)
            elif 'size' in i:
                print(len(stack))
            elif 'empty' in i:
                if stack:
                    print(0)
                else:
                    print(1)
            else:
                if stack:
                    print(stack[-1])
                else:
                    print(-1)
