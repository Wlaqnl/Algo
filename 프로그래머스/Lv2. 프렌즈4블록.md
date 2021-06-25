### Lv2. 프렌즈4블록

---

```python
def delete(arr, block): # 지울 목록, 블록
    global cnt

    while arr:
        x,y=arr.pop()
        if block[x][y]!=0:
            block[x][y]=0
            cnt += 1
        if block[x][y+1]!=0:
            block[x][y+1]=0
            cnt += 1
        if block[x+1][y]!=0:
            block[x+1][y]=0
            cnt += 1
        if block[x+1][y+1]!=0:
            block[x+1][y+1]=0
            cnt += 1
    #print(block)
    return block

def go_down(M,N,block):
    for m in range(M-1,0,-1):
        for n in range(N):
            if block[m][n]==0:
                up=1
                for l in range(m-1,0,-1):
                    if block[l][n]==0:
                        up+=1
                    else:
                        break
                dis=m-up

                #원상 복귀 해줄 count 찾기
                origin=0
                while dis>=0:
                    if block[m][n]!=block[dis][n]:
                        block[m][n]=block[dis][n]
                        block[dis][n]=0
                        m-=1
                        origin+=1
                    else:
                        break
                m+=origin

    return block

def solution(m,n,board):
    global cnt
    cnt=0

    #오른쪽/아래/대각선오른쪽
    dx=[1,0,1]
    dy=[0,1,1]

    block=[]

    for a in range(m):
        new=[]
        for b in board[a]:
            new.append(b)
        block.append(new)
    #print(block)

    while True:
        will_delete = []
        for i in range(m-1):
            for j in range(n-1):
                start=block[i][j]
                if start:
                    for k in range(3):
                        ni=i+dy[k]
                        nj=j+dx[k]
                        if start!=block[ni][nj]:
                            break
                    else:
                        will_delete.append((i,j))

        #print(will_delete)

        if will_delete:
            delete(will_delete,block)
            go_down(m,n,block)
        else:
            break

    return cnt

print(solution(4,5,["CCBDE", "AAADE", "AAABF", "CCBBF"]))
print(solution(6,6,["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]))
```

