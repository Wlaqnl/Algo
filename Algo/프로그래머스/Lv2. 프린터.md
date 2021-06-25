### Lv2. 프린터

---

```python
def solution(priorities, location):
    output=[]
    place=[0]*len(priorities)
    place[location]=1
    flag=False

    while len(priorities)!=0 and not flag:
        a=priorities.pop(0)
        if location==0:
            flag=True

        for i in priorities:
            if i>a:
                priorities.append(a)
                if location==0:
                    place[location]=0
                    place[len(priorities)-1]=1
                    location=len(priorities)-1
                    flag=False
                    break

                else:
                    place[location]=0
                    location-=1
                    place[location]=1
                    break

        else:
            output.append(a)
            if location==0:
                flag=True
            else:
                del place[0]
                location=place.index(1)

    if len(output)==0:
        ans=1
    else:
        ans=len(output)

    return ans
```

