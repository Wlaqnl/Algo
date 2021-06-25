import sys
sys.stdin=open("1992 쿼드트리.txt","r")

def tree(n,x,y):
    global quad, ans

    start=quad[x][y]
    make=True

    for i in range(x,x+n):
        if make:
            for j in range(y, y+n):
                if quad[i][j]!=start:
                    ans+='('
                    tree(n//2, x, y)
                    tree(n//2, x, y+n//2)
                    tree(n//2, x+n//2, y)
                    tree(n//2, x+n//2, y+n//2)
                    make=False
                    ans+=')'
                    break
    if make:
        if start:
            ans+='1'
        else:
            ans+='0'

N=int(input())
quad=[list(map(int,input())) for _ in range(N)]
ans=''
tree(N,0,0)
print(ans)
