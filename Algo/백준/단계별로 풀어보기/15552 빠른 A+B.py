import sys  # sys모듈 읽어들이기
sys.stdin=open("15552 빠른 A+B.txt")
t = int(sys.stdin.readline().rstrip())

for _ in range(t):
    a,b = map(int, sys.stdin.readline().split())
    print(a+b)