### Lv2. 올바른 괄호

---

```python
def solution(s):
    bracket=[]

    for i in s:
        if i=='(':
            bracket.append(i)
        else:
            if bracket:
                bracket.pop()
            else:
                return False
    else:
        if bracket:
            return False
        else:
            return True

print(solution('()()'))
print(solution('(())()'))
print(solution(')()('))
print(solution('(()('))
```

