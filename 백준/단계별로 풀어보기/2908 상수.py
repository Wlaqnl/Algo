import sys
sys.stdin=open("2908 상수.txt","r")

A, B = input().split()

if int(A[::-1])<int(B[::-1]):
    print(int(B[::-1]))
else:
    print(int(A[::-1]))