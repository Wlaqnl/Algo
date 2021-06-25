import sys
sys.stdin=open("9184 신나는 함수 실행.txt","r")

dp=[[[0]*21 for _ in range(21)] for _ in range(21)]

def enjoy(a,b,c):
    if a<=0 or b<=0 or c<=0:
        return 1
    elif a>20 or b>20 or c>20:
        return enjoy(20,20,20)

    if dp[a][b][c]:
        return dp[a][b][c]

    elif a<b and b<c:
        dp[a][b][c]=enjoy(a,b,c-1)+enjoy(a,b-1,c-1)-enjoy(a,b-1,c)
        return dp[a][b][c]
    else:
        dp[a][b][c]=enjoy(a-1,b,c)+enjoy(a-1,b-1,c)+enjoy(a-1,b,c-1)-enjoy(a-1,b-1,c-1)
    return dp[a][b][c]

while True:
    a,b,c = map(int,input().split())
    if a==b==c==-1:
        break
    else:
        print('w({}, {}, {}) = {}'.format(a,b,c,enjoy(a,b,c)))
