### Lv2. 메뉴 리뉴얼

---

```python
from itertools import combinations

def solution(orders, course):
    answer=[]
    n=len(orders)

    for c in course:
        candidate=[]
        menu = {}
        for i in range(n):
            for o in list(combinations(sorted(orders[i]),c)):
                chr=''
                for j in o:
                    chr+=j
                candidate.append(chr)

        for k in candidate:
            if k in menu.keys():
                menu[k]+=1
            else:
                menu[k]=1
        # print(menu)
        menus=sorted(menu.items(), key=lambda x:x[1], reverse=True)
        #print(menus)
        if menus:
            maxV=menus[0][1]
            #print(maxV)
            for a,b in menus:
                if b==maxV and b>=2:
                    answer.append(a)
                else:
                    break

    return sorted(answer)

print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"],[2,3,4]))
print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"],[2,3,5]))
print(solution(["XYZ", "XWY", "WXA"],[2,3,4]))
```

