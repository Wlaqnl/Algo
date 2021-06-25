import sys
sys.stdin=open("1780 종이의 개수.txt","r")

def count(n,x,y):
    global paper, minus_one, zero, one

    make=True
    start=paper[x][y]

    for i in range(x,x+n):
        if make:
            for j in range(y, y+n):
                if paper[i][j]!=start:
                    for a in range(3):
                        for b in range(3):
                            count(n//3, x+a*n//3, y+b*n//3)
                    # count(n//3, x, y)
                    # count(n//3, x, y+n//3)
                    # count(n//3, x, y+n//3*2)
                    # count(n//3, x+n//3, y)
                    # count(n//3, x+n//3, y+n//3)
                    # count(n//3, x+n//3, y+n//3*2)
                    # count(n//3, x+n//3*2, y)
                    # count(n//3, x+n//3*2, y+n//3)
                    # count(n//3, x+n//3*2, y+n//3*2)

                    make=False
                    break

    if make:
        if start==-1:
            minus_one+=1
        elif start==0:
            zero+=1
        else:
            one+=1


N=int(input())
paper=[list(map(int,input().split())) for _ in range(N)]
minus_one=0
zero=0
one=0

count(N,0,0)
print(minus_one)
print(zero)
print(one)