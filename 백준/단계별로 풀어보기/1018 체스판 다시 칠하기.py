import sys
sys.stdin=open("1018 체스판 다시 칠하기.txt","r")
T=int(input())

def check(arr):
    global ans

    cnt1=0
    cnt2=0

    for i in range(8):
        for j in range(8):
            if chess1[i][j]!=arr[i][j] :
                cnt1+=1

            elif chess2[i][j]!=arr[i][j] and cnt2<ans:
                cnt2+=1
    else:
        if ans>min(cnt1, cnt2):
            ans=min(cnt1, cnt2)

for tc in range(T):
    N, M = map(int, input().split())
    board=[list(input()) for _ in range(N)]
    #print(board)
    hori1=['W','B']*4
    hori2=['B','W']*4
    #print(([hori1]+[hori2])*4)
    chess1=([hori1]+[hori2])*4
    chess2=([hori2]+[hori1])*4

    ans=64

    #세로로 갔다가 가로로 가기
    for i in range(M-8+1):
        for j in range(N-8+1):
            new_board = []
            for k in range(8):
                new_board+=[board[j+k][i:i+8]]
            #print(new_board)
            check(new_board)

    print(ans)