import sys
sys.stdin=open("2588 곱셈.txt","r")

n=input()
m=input()
ans=0
cnt=0

for i in range(2,-1,-1):
    value=int(n)*int(m[i])
    ans+=value*(10**cnt)
    cnt+=1
    print(value)

print(ans)