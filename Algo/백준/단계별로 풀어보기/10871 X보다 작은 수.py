import sys
sys.stdin=open("10871 X보다 작은 수.txt","r")

N, X = map(int,input().split())
num=list(map(int,input().split()))
ans=[]

for i in num:
    if i<X:
        ans.append(i)

print(' '.join(map(str,ans)))