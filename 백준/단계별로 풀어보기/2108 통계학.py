from collections import Counter
import sys
sys.stdin=open('2108 통계학.txt',"r")
ipt=sys.stdin.readline
T=int(ipt())

for tc in range(T):
    N=int(ipt())
    num=[]

    for _ in range(N):
        i=int(ipt())
        num.append(i)

    num.sort()

    print(int(round(sum(num)/N,0)))
    print(num[N//2])

    frq=Counter(num).most_common()

    if len(frq)>1:
        if frq[0][1]==frq[1][1]:
            print(frq[1][0])
        else:
            print(frq[0][0])
    else:
        print(frq[0][0])

    print(num[-1]-num[0])