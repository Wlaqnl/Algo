from math import gcd
import sys
sys.stdin=open("2981 검문.txt","r")

N=int(input())
num=[]
new_num=[0]*(N-1)
ans=[]

for _ in range(N):
    num.append(int(input()))
num.sort()

for i in range(1,N):
    new_num[i-1]=(num[i]-num[i-1])
#print(new_num)

for j in range(N-2):
    new_num[j+1]=gcd(new_num[j],new_num[j+1])

for k in range(2,int(new_num[-1]**(1/2))+1):
    if new_num[-1]%k==0:
        ans.append(k)
        if k!=new_num[-1]//k:
            ans.append(new_num[-1]//k)
ans.append(new_num[-1])
ans.sort()

print(' '.join(map(str,ans)))





