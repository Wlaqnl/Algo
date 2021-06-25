### Lv2. 타겟 넘버

---

```python
def solution(numbers, target):
    cnt=0
    def goal(idx, now_num):
        if idx == len(numbers)-1:
            if now_num == target:
                nonlocal cnt
                cnt += 1
            # return cnt

        else:
            goal(idx + 1, now_num + numbers[idx+1])
            goal(idx + 1, now_num - numbers[idx+1])

    goal(-1, 0)

    return cnt
```

* 초깃값부터 넣어주는 것으로 설정했기 때문에 **goal(-1,0)**으로 값을 설정해야한다.