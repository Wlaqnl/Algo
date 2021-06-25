> ### Lv2. 수식 최대화

```python
from itertools import permutations

def solution(exp):
    answer=0
    operater=[]
    new_exp=[]
    num = ''

    for i in range(len(exp)):
        try:
            n=int(exp[i])
            num+=exp[i]
            if i==len(exp)-1:
                new_exp.append(int(num))
        except:
            new_exp.append(int(num))
            new_exp.append(exp[i])
            operater.append(exp[i])
            num=''

    operater=set(operater)
    operater_order=list(permutations(set(operater),len(set(operater))))

    for i in operater_order:
        copy_exp=new_exp[:]
        for opt in i:
            idx=0
            while idx<len(copy_exp):
                if copy_exp[idx]==opt:
                    if opt=='+':
                        cal=int(copy_exp[idx-1])+int(copy_exp[idx+1])
                    elif opt=='-':
                        cal = int(copy_exp[idx - 1]) - int(copy_exp[idx + 1])
                    else:
                        cal = int(copy_exp[idx - 1]) * int(copy_exp[idx + 1])
                    copy_exp=copy_exp[:idx-1]+list(str(cal).split())+copy_exp[idx+2:]
                else:
                    idx+=1
        else:
            answer=max(answer,abs(int(copy_exp[0])))

    return answer

print(solution("100-200*300-500+20"))
print(solution("50*6-3*2"))
```

