### Lv2. 카펫

---

```python
def solution(brown, yellow):
    total = brown+yellow
    
    for i in range(1,total//2):
        if total%i==0:
            M,N=i,total//i
            if 2*(M+N)-4 == brown and M*N-2*(M+N)+4 == yellow:
                break

    return [max(M,N),min(M,N)]
```

