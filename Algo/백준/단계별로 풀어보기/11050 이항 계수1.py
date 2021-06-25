import sys
sys.stdin=open('11050 이항 계수1.txt',"r")

N, K = map(int,input().split())
ans=1

for i in range(K):
    ans*=N-i
    ans//=i+1
print(ans)