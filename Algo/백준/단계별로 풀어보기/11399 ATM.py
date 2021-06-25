import sys
sys.stdin=open("11399 ATM.txt","r")

N=int(input())
people=list(map(int,input().split()))
people.sort()

withdraw=[0]*(N)
withdraw[0]=people[0]

for i in range(N-1):
    withdraw[i+1]=withdraw[i]+people[i+1]

print(sum(withdraw))