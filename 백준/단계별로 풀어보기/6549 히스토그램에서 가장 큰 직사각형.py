import sys
sys.stdin=open("6549 히스토그램에서 가장 큰 직사각형.txt","r")

# 시간초과
# while True:
#     histo=list(map(int,input().split()))
#     N=histo.pop(0)
#     if N==0:
#         break
#
#     idx=0
#     max_area=0
#
#     while idx<len(histo)-1:
#         now=histo[idx]
#         cnt=1
#         for i in range(idx+1,len(histo)):
#             if now<=histo[i]:
#                 cnt+=1
#                 if i==len(histo)-1:
#                     idx+=1
#                     if max_area < cnt * now:
#                         max_area = cnt * now
#                         break
#
#             else:
#                 idx+=1
#                 if max_area<cnt*now:
#                     max_area=cnt*now
#                 break
#     print(max_area)

while True:
  n=list(map(int,input().split()))+[0]
  N=n[0]
  if N==0:
    break
  arr=[(1,n[1])]
  answer=0
  for i in range(2,N+2):
    cur=i
    while arr and arr[-1][1]>n[i]:
      cur,h=arr.pop()
      answer=max(answer,(i-cur)*h)
    arr.append((cur,n[i]))
  print(answer)


