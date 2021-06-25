import sys
sys.stdin=open("1747 소수&팰린드롬.txt","r")

N=int(input())
state=True

if N==1:
    print(2)
elif N==2:
    print(2)
else:
    for i in range(N,1005001):
        if i%2!=0 and state:
            for j in range(2,int(i**(1/2))+1):
                if i%j==0:
                    break
            else:
                if str(i)==str(i)[::-1]:
                    print(i)
                    state=False




