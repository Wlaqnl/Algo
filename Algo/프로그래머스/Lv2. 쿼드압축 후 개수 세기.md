### Lv2. 쿼드압축 후 개수 세기

---

```python
def check(arr):
    flag=True
    n=len(arr)
    k = arr[0][0]

    if n!=1:
        for i in range(n):
            if flag:
                for j in range(n):
                    if arr[i][j]==k:
                        continue
                    else:
                        flag=False
                        break

    else:
        if k:
            answer[k]+=1
        else:
            answer[k]+=1
        return answer

    if not flag:
        a=[]
        b=[]
        c=[]
        d=[]
        for i in range(n):
            if i<n//2:
                a.append(arr[i][:n//2])
                b.append(arr[i][n//2:])
            else:
                c.append(arr[i][:n//2])
                d.append(arr[i][n//2:])
        check(a)
        check(b)
        check(c)
        check(d)

    if flag:
        answer[k]+=1


def solution(arr):
    global answer
    answer = [0, 0]
    check(arr)
    return answer
```



