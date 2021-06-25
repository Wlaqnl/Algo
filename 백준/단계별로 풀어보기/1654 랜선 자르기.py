import sys
sys.stdin=open("1654 랜선 자르기.txt","r")

K,N =map(int,input().split())
Lansun=[]
for _ in range(K):
    Lansun.append(int(input()))

Lansun.sort()
start=1 #스타트 1로해야 zero divison 오류 발생하지 않음
end=Lansun[-1]
ans=0

while start<=end:
    mid=(start+end)//2
    cnt=0

    for i in Lansun:
        #크거나 같아야함!
        if mid<=i:
            cnt+=i//mid

    if cnt>=N:
        start=mid+1
        if ans<mid:
            ans=mid
    else:
        end=mid-1

print(ans)