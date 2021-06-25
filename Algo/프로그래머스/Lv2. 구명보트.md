### Lv2. 구명보트

---

> 통과한 코드

```python
def solution(people, limit):
    people.sort()
    light=0
    heavy=len(people)-1
    count=0
    while(light<heavy):
        if people[light]+people[heavy]<=limit:
            count+=1
            light+=1
            heavy-=1
        else:
            heavy-=1
    return len(people)-count
```

* 제일 무거운 사람과 제일 가벼운 사람을 매칭시켜서 최대 견딜 수 있는 무게와 비교해보는 방식



> 못 통과한 코드

```python
def solution(people, limit):
    people.sort(reverse=True)
    answer=0
    visit=[0]*len(people)

    '''최적의 방법
    사람들의 몸무게를 내림차순으로 정렬한 뒤
    그 해당 몸무게와 같이 탈 수 있는 다른 사람의 몸무게의 최대값을 구해서
    존재하면 같이 구명보트에 태우고
    아니면 그냥 둔다.
    마지막에는 태우지 못한 사람들만 visit list에 남아 있을 것이니까 그것만 더하면 된다.
    => 시간 초과 ^_^'''

    for idx, weight in enumerate(people):
        if visit[idx]==0:
            second_person = limit-weight

        else:
            continue

        if people[-1]<=second_person:
            for i in range(idx+1,len(people)):
                if people[i]<=second_person and visit[i]==0:
                    second_idx=i
                    visit[second_idx]=1
                    visit[idx]=1
                    answer+=1
                    break

    answer+=visit.count(0)

    return answer
```

