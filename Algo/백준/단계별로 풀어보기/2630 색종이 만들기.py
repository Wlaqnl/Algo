import sys
sys.stdin=open("2630 색종이 만들기.txt","r")

def colored_paper(n, arr, i, j):
    global white, blue

    start=arr[i][j]
    make=True

    for y in range(i,i+n):
        if make:
            for x in range(j,j+n):
                if arr[y][x]!=start:
                    colored_paper(n//2, arr, i, j)
                    colored_paper(n//2, arr, i+n//2, j)
                    colored_paper(n//2, arr, i, j+n//2)
                    colored_paper(n//2, arr, i+n//2, j+n//2)
                    make=False
                    break
    else:
        if make:
            if start:
                blue+=1
            else:
                white+=1


N=int(input())
paper=[list(map(int,input().split())) for _ in range(N)]
white=0
blue=0

colored_paper(N, paper, 0,0)
print(white)
print(blue)