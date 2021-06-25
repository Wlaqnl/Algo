import sys
sys.stdin=open("2565 전깃줄.txt","r")

n=int(input())
wire=[]
second_wire=[]
dp=[0 for _ in range(n)]

for _ in range(n):
    wire.append(list(map(int,input().split())))
#print(wire)
wire.sort(key=lambda x:x[0])
#print(wire)

for w in wire:
    second_wire.append(w[1])
#print(second_wire)

for i in range(n):
    for j in range(i):
        if second_wire[i]>second_wire[j] and dp[i]<dp[j]:
            dp[i]=dp[j]
    dp[i]+=1
print(n-max(dp))
