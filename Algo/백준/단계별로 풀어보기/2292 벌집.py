import sys
sys.stdin=open("2292 벌집.txt","r")

n=int(input())
honeycomb=[1]
i=1
k=0

while i<1000000000:
    honeycomb.append(i+6*k+1)
    i=i+6*k
    k+=1
#print(honeycomb)

for j in range(len(honeycomb)-1):
    if honeycomb[j]<=n<honeycomb[j+1]:
        print(j+1)
        break
