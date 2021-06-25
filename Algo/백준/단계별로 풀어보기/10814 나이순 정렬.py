import sys
sys.stdin=open("10814 나이순 정렬.txt","r")

N=int(input())
member=[]

for _ in range(N):
    a, b = input().split()
    member.append((int(a),b))

members=sorted(member, key=lambda x:x[0])
#print(members)

for m in members:
    print(m[0],m[1])