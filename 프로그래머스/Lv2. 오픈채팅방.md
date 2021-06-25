### Lv2. 오픈채팅방

---

```python
def solution(record):
    user_state = {}
    user_name = {}

    # 최종 이름 결정짓기
    for r in record:
        chat = r.split()
        if len(chat) == 3:
            a, b, c = chat
            user_name[b] = c

    # 출력을 위한 과정
    ans = []
    for r in record:
        chat = r.split()
        if len(chat) == 2:
            doing, name = chat
            sentence = user_name[name] + '님이 나갔습니다.'
            ans.append(sentence)
        else:
            doing, id, name = chat
            if doing == 'Enter':
                sentence = user_name[id] + '님이 들어왔습니다.'
                ans.append(sentence)

    return ans

print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))
```

