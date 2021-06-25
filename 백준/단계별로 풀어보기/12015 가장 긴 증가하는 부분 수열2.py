import sys
sys.stdin=open('12015 가장 긴 증가하는 부분 수열2.txt',"r")

def findlow(num):
    l=0
    h=len(lis)-1
    ret=1000000

    while l<=h:
        mid=(l+h)//2
        if lis[mid]>=num:
            if ret>mid:
                ret=mid
            h=mid-1
        else:
            l=mid+1
    return ret

N=int(input())
suyeol=list(map(int,input().split()))
lis=[suyeol[0]]

for i in range(1, N):
    if lis[len(lis)-1]<suyeol[i]:
        lis.append(suyeol[i])
    else:
        lis[findlow(suyeol[i])]=suyeol[i]

#print(lis)
print(len(lis))