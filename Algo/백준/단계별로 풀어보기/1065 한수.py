import sys
sys.stdin=open("1065 한수.txt","r")
T=int(input())

for tc in range(T):
    n=int(input())
    ans=[]
    k=111
    cnt=0

    for i in range(1,100):
        ans.append(i)

    while k<=999:
        check=k
        jarisu=[]
        while k>=10:
            jarisu.append(k%10)
            k=k//10
        jarisu.append(k)

        if jarisu[1]-jarisu[0]==jarisu[2]-jarisu[1]:
            ans.append(check)
        k=check+1

    for i in ans:
        if i<=n:
            cnt+=1
        else:
            break
    print(cnt)


