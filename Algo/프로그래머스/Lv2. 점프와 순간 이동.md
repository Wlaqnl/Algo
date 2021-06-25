### Lv2. 점프와 순간 이동

---

```python
def solution(n):
    battery=1

    while n!=1:
        if n%2:
            n-=1
            battery+=1
        else:
            n=n//2
    return battery

print(solution(5))
print(solution(6))
print(solution(5000))
```

