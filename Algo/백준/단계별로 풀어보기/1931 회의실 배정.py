import sys
sys.stdin=open("1931 회의실 배정.txt","r")

N=int(input())
conference=[]
last=0
cnt=0

for _ in range(N):
    conference.append(list(map(int, sys.stdin.readline().split())))

# 빨리 끝나는 회의 순서대로 정렬하는 것이 가장 많은 회의의 수를 알 수 있다.
conference.sort(key=lambda x:(x[1],x[0]))
#print(conference)

for i,j in conference:
    if i>=last:
        cnt+=1
        last=j
print(cnt)
