import sys,math
sys.stdin=open("2581 소수.txt","r")
T=int(input())

for tc in range(T):
    M=int(input())
    N=int(input())
    sosu=[]
    ans=0

    for i in range(M, N+1):
        if i!=1:
            for j in range(2, int(math.sqrt(i))+1):
                if i%j==0:
                    break
            else:
                sosu.append(i)
    #print(sosu)

    if sosu:
        for k in sosu:
            ans+=k
        print(ans)
        print(min(sosu))
    else:
        print(-1)


