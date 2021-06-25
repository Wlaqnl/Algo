import sys
sys.stdin=open("4949 균형잡힌 세상.txt","r")

while True:
    s=input()
    if s=='.':
        break
    #print(s)
    stack=[]

    for i in s:
        if i=='(' or i=='[':
            stack.append(i)
        elif i==')':
            if stack and stack[-1]=='(':
                stack.pop()
            else:
                print('no')
                break
        elif i==']':
            if stack and stack[-1]=='[':
                stack.pop()
            else:
                print('no')
                break
    else:
        if stack:
            print('no')
        else:
            print('yes')
