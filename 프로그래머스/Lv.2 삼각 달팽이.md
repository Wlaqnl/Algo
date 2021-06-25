### Lv.2 삼각 달팽이

---

```python
def solution(n):
    snail = [[0]*n for _ in range(n)]
    final_num=(n**2+n)//2
    cnt=1
    way=1
    dot_x=0
    dot_y=0
    answer=[]

    while cnt<=final_num:
        if way==1:
            if snail[dot_y][dot_x]==0:
                snail[dot_y][dot_x]=cnt
                for i in range(n):
                    dot_y+=1
                    cnt+=1
                    if dot_y<n and snail[dot_y][dot_x]==0:
                            snail[dot_y][dot_x]=cnt
                    else:
                        way=2
                        dot_x+=1
                        dot_y-=1
                        break
            else:
                break

        elif way==2:
            if snail[dot_y][dot_x]==0:
                snail[dot_y][dot_x]=cnt
                for i in range(n):
                    dot_x+=1
                    cnt+=1
                    if dot_x<n and snail[dot_y][dot_x]==0:
                            snail[dot_y][dot_x]=cnt
                    else:
                        way=3
                        dot_x-=2
                        dot_y-=1
                        break
            else:
                break


        else:
            if snail[dot_y][dot_x]==0:
                snail[dot_y][dot_x]=cnt
                for i in range(n):
                    dot_x-=1
                    dot_y-=1
                    cnt+=1
                    if 0<=dot_x<n and 0<=dot_y<n and snail[dot_y][dot_x]==0:
                            snail[dot_y][dot_x]=cnt
                    else:
                        way=1
                        dot_x+=1
                        dot_y+=2
                        break
            else:
                break

    for triangle in snail:
        for i in triangle:
            if i!=0:
                answer.append(i)

    return answer
```

