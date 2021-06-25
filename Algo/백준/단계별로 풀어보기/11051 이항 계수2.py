import sys
sys.stdin=open('11051 이항 계수2.txt',"r")

N, K = map(int,input().split())
ans=1

for i in range(K):
    ans*=N-i
    ans//=i+1
print(ans%10007)