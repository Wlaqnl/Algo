import sys
sys.stdin=open("10773 제로.txt","r")
T=int(input())

for tc in range(T):
    n=int(input())
    dining=[]
    
    for _ in range(n):
        money=int(input())
        if money:
            dining.append(money)
        else:
            dining.pop()
    print(sum(dining))