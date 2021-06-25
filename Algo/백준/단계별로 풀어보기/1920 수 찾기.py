import sys
sys.stdin=open("1920 수 찾기.txt","r")

def find(target, arr, start, end):
    while start<=end:
        mid=(start+end)//2

        if arr[mid]==target:
            return mid

        elif arr[mid]>target:
            end=mid-1

        else:
            start=mid+1
    return None

N=int(input())
num_list=list(map(int,input().split()))
num_list.sort()

M=int(input())
num=list(map(int,input().split()))

for n in num:
    result=find(n,num_list, 0, N-1)

    if result == None:
        print(0)
    else:
        print(1)