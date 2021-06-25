### Lv2. 전화번호 목록

---

```python
def solution(phone_book):
    answer=True
    num=sorted(phone_book)
    Flag=True

    for i in range(len(num)-1):
        if Flag:
            for j in range(i+1,len(num)):
                if num[i] == num[j][:len(num[i])]:
                    answer=False
                    Flag=False
                    break

    return answer

print(solution(['119', '97674223', '1195524421']))
print(solution(['123','456','789']))
print(solution(['12','123','1235','567','88']))
```

