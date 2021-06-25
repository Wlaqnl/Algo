### Lv2. n진수 게임

---

```python
def jinsu_change(num,N):
    Notation='0123456789ABCDEF'
    q,r=divmod(num,N)
    n=Notation[r]
    return jinsu_change(q,N)+n if q else n

def solution(n,t,m,p):
    num_list=[]
    cnt=0
    ans=''

    #문제에 따른 t*m의 최댓값은 10^5
    while len(num_list)<=t*m:
        num=jinsu_change(cnt,n)
        for i in num:
            num_list.append(i)
        cnt+=1
    #print(num_list)

    for j in range(p-1,len(num_list),m):
        ans+=(num_list[j])
        if len(ans)==t:
            break

    return ans

print(solution(2,4,2,1))
print(solution(16,16,2,1))
print(solution(16,16,2,2))
```

