import sys
sys.stdin=open('1874 스택 수열.txt',"r")
T=int(input())

for tc in range(T):
    #pypy로 하면 통과, python으로는 불통과
    # n=int(input())
    # sequence=[]
    # stack=[]
    # ans=[]
    # cnt=0
    # output=[]
    # temp=True
    #
    # for _ in range(n):
    #     sequence.append(int(input()))
    #
    # # print(sequence)
    #
    # for s in sequence:
    #     if s>=cnt:
    #         for i in range(cnt+1,s+1):
    #             stack.append(i)
    #             output.append('+')
    #         cnt=s
    #         ans.append(stack.pop())
    #         output.append('-')
    #     else:
    #         if s in stack and stack[-1]==s:
    #             ans.append(stack.pop())
    #             output.append('-')
    #         else:
    #             temp=False
    #             break
    # if temp:
    #     for o in output:
    #         print(o)
    # else:
    #     print('NO')

    n = int(input())
    s = []
    op = []
    count = 1
    temp = True
    for i in range(n):
        num = int(input())
        while count <= num:
            s.append(count)
            op.append('+')
            count += 1
        if s[-1] == num:
            s.pop()
            op.append('-')
        else:
            temp = False
    if temp == False:
        print('NO')
    else:
        for i in op:
            print(i)