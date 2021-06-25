from itertools import combinations
import sys
sys.stdin=open("2309 일곱 난쟁이.txt","r")

height=[]

for _ in range(9):
    height.append(int(input()))
height.sort()

dwarf=combinations(height,7)

for i in dwarf:
    if sum(i)==100:
        ans=i
        break

for a in ans:
    print(a)