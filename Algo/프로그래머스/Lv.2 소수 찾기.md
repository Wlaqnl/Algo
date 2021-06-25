> ### Lv.2 소수 찾기

```python
from itertools import permutations

def solution(numbers):
    scul=[]
    cnt=0

    for i in range(len(numbers)+1):
        paper=permutations(list(numbers),i)

        for j in list(paper):
            num=''.join(map(str,list(j)))
            if num:
                if int(num) not in scul and int(num)!=0 and int(num)!=1:
                    scul.append(int(num))
    #print(scul)

    for k in scul:
        for m in range(2, k//2+1):
            if k%m==0:
                break
        else:
            cnt+=1

    return cnt
```

