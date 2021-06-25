import sys
sys.stdin=open("만들 수 없는 금액.txt","r")

N=int(input())
bill=list(map(int,input().split()))
bill.sort()
money=[0]*(sum(bill)+1)
money[bill[0]]=1
#print(money)

for b in range(1, len(bill)):
    idx=money[1:].index(0)+1
    for i in range(1,idx):
        if money[i]==1 and i+bill[b]<len(money):
            money[i+bill[b]]=1

    if money[bill[b]]==0:
        money[bill[b]]=1

if 0 not in money[1:]:
    print(sum(bill)+1)
else:
    print(money[1:].index(0)+1)