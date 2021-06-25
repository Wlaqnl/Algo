### Lv2. 예상 대진표

---

```python
def solution(n,a,b):
    answer=1

    while abs(a-b)>1 or (abs(a-b)==1 and a//2==b//2):
        if a%2:
            a=(a+1)//2
        else:
            a//=2
        if b%2:
            b=(b+1)//2
        else:
            b//=2
        answer+=1

    return answer

print(solution(8,4,7)) 3
print(solution(8,1,2)) 1
print(solution(8,2,3)) 2
print(solution(8,2,1)) 1
print(solution(16,8,9)) 4
```

