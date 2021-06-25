### Lv2. 폰켓몬

---

```python
from itertools import combinations

def solution(nums):
    # n=len(nums)//2
    # phoneketmon=list(combinations(nums,n))
    # ans=0
    #
    # for p in phoneketmon:
    #     if len(set(p))>ans:
    #         ans=len(set(p))
    # return ans

    ans=len(nums)//2
    mon=set(nums)
    #print(mon)

    if ans>len(mon):
        ans=len(mon)

    return ans

print(solution([3,1,2,3]))
print(solution([3,3,3,2,2,4]))
print(solution([3,3,3,2,2,2]))
```

