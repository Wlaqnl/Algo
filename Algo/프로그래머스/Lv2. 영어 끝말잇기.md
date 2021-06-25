### Lv2. 영어 끝말잇기

---

```python
def solution(n, words):
    turn=0
    word_chain=[]
    flag=True

    while words and flag:
        turn+=1
        for i in range(n):
            now=i+1
            if not word_chain:
                word_chain.append(words.pop(0))
            else:
                if word_chain[-1][-1]==words[0][0] and words[0] not in word_chain:
                    word_chain.append(words.pop(0))
                else:
                    flag=False
                    break

    if flag:
        return [0,0]

    else:
        return [now,turn]


print(solution(3,['tank', 'kick', 'know', 'wheel', 'land', 'dream', 'mother', 'robot', 'tank']))
print(solution(5,['hello', 'observe', 'effect', 'take', 'either', 'recognize', 'encourage', 'ensure', 'establish', 'hang', 'gather', 'refer', 'reference', 'estimate', 'executive']))
print(solution(2,['hello', 'one', 'even', 'never', 'now', 'world', 'draw']))
```

