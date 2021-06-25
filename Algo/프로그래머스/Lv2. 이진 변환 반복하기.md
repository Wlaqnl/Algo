### Lv2. 이진 변환 반복하기

---

```python
def solution(s):
    cnt_0=0
    change=0
    while s!='1':
        change+=1
        ones=0
        for i in s:
            if i=='1':
                ones+=1
            else:
                cnt_0+=1
        res=format(bin(ones)[2:])
        #print(res)
        s=res

    return [change,cnt_0]

print(solution("110010101001"))
print(solution("01110"))
print(solution("1111111"))
```

