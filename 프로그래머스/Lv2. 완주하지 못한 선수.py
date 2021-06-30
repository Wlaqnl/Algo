#해쉬 이용
def solution(participant, completion):
    answer = ''
    temp = 0
    dic = {}
    for part in participant:
        dic[hash(part)] = part
        temp += int(hash(part))
    for com in completion:
        temp -= hash(com)
    answer = dic[temp]

    return answer

print(solution(["leo", "kiki", "eden"],["eden", "kiki"]))

#zip 이용
def solution(participant, completion):
    participant.sort()
    completion.sort()

    for p, c in zip(participant, completion):
        if p != c:
            return p
    return participant.pop()

#counter 이용
import collections as col

def solution(participant, completion):
    return list((col.Counter(participant) - col.Counter(completion)).keys())[0]