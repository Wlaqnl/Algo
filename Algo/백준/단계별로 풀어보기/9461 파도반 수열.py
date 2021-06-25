import sys
sys.stdin=open("9461 파도반 수열.txt","r")
T=int(input())

for tc in range(T):
    N=int(input())
    wave=[0]*101
    wave[0]=0
    wave[1]=1
    wave[2]=1

    if N>=3:
        for i in range(3,N+1):
            wave[i]=wave[i-3]+wave[i-2]
    print(wave[N])