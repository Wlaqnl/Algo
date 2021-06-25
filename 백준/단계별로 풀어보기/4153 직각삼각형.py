import sys
sys.stdin=open('4153 직각삼각형.txt','r')


while True:
    a,b,c=map(int,input().split())
    if a==b==c==0:
        break
    else:
        side = []
        side.append(a)
        side.append(b)
        side.append(c)
        side.sort()
        if (side[0]**2)+(side[1]**2)==(side[2]**2):
            print('right')
        else:
            print('wrong')
