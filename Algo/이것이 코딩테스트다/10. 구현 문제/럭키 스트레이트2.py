import sys
sys.stdin=open("럭키 스트레이트.txt","r")
T=int(input())

for tc in range(T):
    n=input()
    length=len(n)
    summary=0

    for i in range(length//2):
        summary+=int(n[i])

    for i in range(length//2, length):
        summary-=int(n[i])

    if summary==0:
        print("LUCKY")
    else:
        print("READY")