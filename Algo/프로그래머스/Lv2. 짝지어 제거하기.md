### Lv2. 짝지어 제거하기

---

```python
def solution(s):
    pair=[]

    for i in s:
        if pair:
            if pair[-1]!=i:
                pair.append(i)
            else:
                pair.pop(-1)
        else:
            pair.append(i)
    if pair:
        return 0
    else:
        return 1

print(solution('baabaa'))
print(solution('cdcd'))
```

