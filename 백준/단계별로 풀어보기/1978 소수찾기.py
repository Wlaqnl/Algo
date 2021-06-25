import sys
sys.stdin=open("1978 소수찾기.txt","r")

N=int(input())
num=list(map(int,input().split()))
ans=0

for n in num:
    if n==1:
        continue
    else:
        for i in range(2,n):
            if n%i==0:
                break
        else:
            ans+=1
print(ans)