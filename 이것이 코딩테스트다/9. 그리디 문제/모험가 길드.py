import sys
sys.stdin=open("모험가 길드.txt","r")

N=int(input())
data=list(map(int,input().split()))
data.sort()

result=0 #그룹 수
count=0 # 모험가의 수

for i in data:
    count+=1
    if count >= i:
        result+=1
        count=0

print(result)

