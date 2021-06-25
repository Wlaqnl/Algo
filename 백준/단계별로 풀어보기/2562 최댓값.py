import sys
sys.stdin=open("2562 최댓값.txt","r")

num=[]
for _ in range(9):
    num.append(int(input()))
print(max(num))
print(num.index(max(num))+1)