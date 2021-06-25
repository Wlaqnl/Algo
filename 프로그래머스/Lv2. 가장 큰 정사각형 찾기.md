### Lv2. 가장 큰 정사각형 찾기

---

```python
def solution(board):
    n=len(board)
    m=len(board[0])
    maxV=0

    #1*1 일 때
    if n==m==1:
        if board[0][0]==1:
            return 1

    else:
        for i in range(1,n):
            for j in range(1,m):
                if board[i][j]==0:
                    continue
                else:
                    k=min(board[i-1][j-1], board[i-1][j], board[i][j-1])
                    board[i][j]=k+1
                    if board[i][j]>maxV:
                        maxV=board[i][j]

    return maxV*maxV

print(solution([[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]]))
print(solution([[0,0,1,1],[1,1,1,1]]))
```

