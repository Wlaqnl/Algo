import sys
sys.stdin=open("10952 A+B-5.txt","r")

while True:
    a, b = map(int, input().split())
    if a==0 and b==0:
        break
    else:
        print(a+b)
