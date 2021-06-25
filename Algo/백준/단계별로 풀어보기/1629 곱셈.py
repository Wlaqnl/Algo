import sys
sys.stdin=open("1629 곱셈.txt","r")

A, B, C = map(int,input().split())
#(A^B)%C 출력
#큰 수 계산할 때만 pow가 빠르다.
print(pow(A,B,C))