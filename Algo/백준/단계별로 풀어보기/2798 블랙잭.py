from itertools import combinations
import sys
sys.stdin=open("2798 블랙잭.txt","r")
T=int(input())


for tc in range(T):
    N, M = map(int,input().split())
    cards=list(map(int,input().split()))
    cards.sort(reverse=True)
    maxV=0
    #print(cards)
    for card in combinations(cards,3):
        if sum(card)==M:
            maxV=M
            break
        elif sum(card)<M:
            if maxV<sum(card):
                maxV=sum(card)
    print(maxV)




