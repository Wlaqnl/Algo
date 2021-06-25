import sys
sys.stdin=open("2110 공유기 설치.txt","r")

N, C = map(int,input().split())
house=[int(input()) for _ in range(N)]
house.sort()

start=1
end=house[-1]-house[0]
result=0

while start<=end:
    mid=(start+end)//2
    value=house[0]
    count=1

    for i in range(1,N):
        if house[i]>=value+mid:
            value=house[i]
            count+=1
    if count>=C:
        start=mid+1
        result=mid
    else:
        end=mid-1
print(result)