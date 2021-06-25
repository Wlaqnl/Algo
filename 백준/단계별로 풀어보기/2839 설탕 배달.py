import sys
sys.stdin=open("2839 설탕 배달.txt","r")
T=int(input())

for tc in range(T):
    kg=int(input())
    cnt=0

    while kg>=0:
        if kg%5==0:
            cnt+=kg//5
            print(cnt)
            break
        kg-=3
        cnt+=1
    else:
        print(-1)





