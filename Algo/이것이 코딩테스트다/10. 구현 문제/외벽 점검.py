from itertools import permutations

def solution(n, weak, dist):
    #길이를 2배 늘려서 '원형'을 일자 형태로 변형
    length=len(weak)
    for i in range(length):
        weak.append(weak[i]+n)
    answer=len(dist)+1

    for start in range(length):
        for friends in list(permutations(dist, len(dist))):
            count=1
            position = weak[start]+friends[count-1]

            for index in range(start, start+length):
                if position<weak[index]:
                    count+=1
                    if count>len(dist):
                        break
                    position=weak[index]+friends[count-1]
            answer = min(answer, count)

    if answer>len(dist):
        return -1
    return answer

print(solution(12,[1, 5, 6, 10],[1, 2, 3, 4]))
print(solution(12,[1, 3, 4, 9, 10], [3, 5, 7]))