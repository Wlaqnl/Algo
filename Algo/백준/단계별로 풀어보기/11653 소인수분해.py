import sys,math
sys.stdin=open('11653 소인수분해.txt',"r")
T=int(input())

for tc in range(T):
    # 시간초과
    # n=int(input())
    # sosu=[True for i in range(n+1)]
    # sosu[1]=0
    # ans=[]
    #
    # for i in range(2, int(math.sqrt(n+1))+1):
    #     if sosu[i]==True:
    #         j=2
    #         while i*j <= n:
    #             sosu[i*j]=False
    #             j+=1
    #
    # while n!=1:
    #     for s in range(2,len(sosu)):
    #         if sosu[s]==True:
    #             if n%s==0:
    #                 ans.append(s)
    #                 n=n//s
    #                 break
    #
    # for k in ans:
    #     print(k)
    v=int(input())
    i=2
    while v!=1:
        if v%i==0:
            v=v/i
            print(i)
        else:
            i+=1