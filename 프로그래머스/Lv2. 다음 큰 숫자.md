### Lv2. 다음 큰 숫자

---

```python
def solution(n):
    cnt_1=format(n,'b').count('1')

    for i in range(n+1, 1000001):
        if cnt_1==format(i,'b').count('1'):
            break

    return i

print(solution(78))
print(solution(15))
```

