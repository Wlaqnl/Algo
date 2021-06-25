### Lv2. 피보나치 수

---

```python
def solution(x):
    d = [0] * (x+1)
    d[1]=1
    d[2]=1

    for i in range(3,x+1):
        d[i]=d[i-1]+d[i-2]
        
    return d[-1]%1234567


print(solution(3))
print(solution(5))
```

* 이 문제는 재귀 사용하면 런타임 에러 발생