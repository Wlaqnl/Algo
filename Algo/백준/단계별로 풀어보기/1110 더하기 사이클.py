import sys
sys.stdin=open("1110 더하기 사이클.txt","r")

T=int(input())

for tc in range(T):
    n=int(input())
    a=100
    cnt=0

    while a!=n:
        if cnt==0:
            a=n
        if a<10:
            plus=str(a)
        else:
            plus=str(int(str(a)[0])+int(str(a)[1]))[-1]
        a=int(str(a)[-1]+plus)
        cnt+=1

    print(cnt)