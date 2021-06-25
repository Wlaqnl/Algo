import sys
sys.stdin=open('2751 수 정렬하기2.txt',"r")

# 시간초과 나요 ㅠㅠ
# N=int(input())
# num=[]
#
# for _ in range(N):
#     num.append(int(input()))
# num.sort()
#
# for n in num:
#     print(n)

ipt = sys.stdin.readline
arr = []

for i in range(int(ipt())):
    arr.append(int(ipt()))

arr = sorted(arr)

for i in arr:
    print(i)

