import sys,math
sys.stdin=open("2869 달팽이는 올라가고 싶다.txt","r")

A, B, V = map(int,input().split())

day=(V-B)/(A-B)

print(math.ceil(day))