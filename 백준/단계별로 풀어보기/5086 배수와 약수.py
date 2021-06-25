import sys
sys.stdin=open("5086 배수와 약수.txt","r")

while True:
    A, B = map(int,input().split())
    if A==B==0:
        break
    else:
        if A>B and A%B==0:
            print('multiple')
        elif A<B and B%A==0:
            print('factor')
        else:
            print('neither')



