import sys
sys.stdin=open('3009 네 번째 점.txt',"r")

spot=[[] for _ in range(2)]
ans=[]

for _ in range(3):
    A, B = map(int,input().split())
    spot[0].append(A)
    spot[1].append(B)

for i in spot:
    for j in i:
        if i.count(j)==1:
            ans.append(j)
            break

print(' '.join(map(str,ans)))

