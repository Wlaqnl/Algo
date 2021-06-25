import sys
sys.stdin=open("8958 OX퀴즈.txt","r")
T=int(input())

for tc in range(T):
    result=input()
    cnt=0
    ans=0

    for i in result:
        if i=='O':
            cnt+=1
            ans+=cnt
        else:
            cnt=0

    print(ans)