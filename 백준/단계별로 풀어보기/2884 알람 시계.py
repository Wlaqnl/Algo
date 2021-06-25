import sys
sys.stdin=open("2884 알람 시계.txt","r")

H, M = map(int,input().split())

if M>=45:
    M-=45
else:
    M=60-(45-M)
    if H==0:
        H=23
    else:
        H-=1

print(H, M)