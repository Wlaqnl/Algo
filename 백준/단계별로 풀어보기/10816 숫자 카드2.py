import sys
sys.stdin=open("10816 숫자 카드2.txt","r")

#이분 탐색
# def find(arr, target, start, end):
#     while start<=end:
#         mid=(start+end)//2
#
#         if arr[mid]==target:
#             return arr[start:end+1].count(target)
#         elif arr[mid]>target:
#             end=mid-1
#         else:
#             start=mid+1
#     if start>end:
#         return 0
#     return None
#
# N=int(input())
# num_list=list(map(int,sys.stdin.readline().split()))
# num_list.sort()
#
# M=int(input())
# num=list(map(int,sys.stdin.readline().split()))
#
# ans={}
#
# #중복 처리 해야 시간초과 안뜸!
# for n in num:
#     if n not in ans:
#         ans[n]=find(num_list, n, 0, N-1)
#
# print(' '.join(str(ans[x]) if x in ans else '0' for x in num))

#해쉬 알고리즘
N=int(input())
num_list=list(map(int,sys.stdin.readline().split()))
num_list.sort()

M=int(input())
num=list(map(int,sys.stdin.readline().split()))

hashmap={}
for n in num_list:
    if n in hashmap:
        hashmap[n]+=1
    else:
        hashmap[n]=1

print(' '.join(str(hashmap[m]) if m in hashmap else '0' for m in num))