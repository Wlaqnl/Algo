from itertools import combinations,permutations
import sys
sys.stdin=open("14889 스타트와 링크.txt","r")
T=int(input())

for tc in range(T):
    n=int(input())
    skill=[list(map(int,input().split())) for _ in range(n)]
    people=[i+1 for i in range(n)]
    team=list(combinations(people,n//2))
    ans=1e9

    for t in range(len(team)//2):
        start = list(permutations(team[t],2))
        link = list(permutations(team[len(team)-t-1],2))
        S=0
        L=0
        #print(start)
        #print(link)

        for s in start:
            a,b=s
            S+=skill[a-1][b-1]

        for l in link:
            c,d=l
            L+=skill[c-1][d-1]

        if abs(S-L)<ans:
            ans=abs(S-L)

    print(ans)