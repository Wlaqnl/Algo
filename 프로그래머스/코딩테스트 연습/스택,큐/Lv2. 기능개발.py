def solution(progresses, speeds):
    day=[]
    answer = []
    N=len(progresses)

    for i in range(N):
        d = (100 - progresses[i]) // speeds[i]
        r = (100 - progresses[i]) % speeds[i]
        if r==0:
            day.append(d)
        else:
            day.append(d+1)

    i=0
    while i<len(day):
        a=day[i]
        i+=1
        cnt=1
        if i<len(day):
            for j in range(i,len(day)):
                if day[j]<=a:
                    cnt+=1
                    i+=1
                else:
                    answer.append(cnt)
                    break
            else:
                answer.append(cnt)
        else:
            answer.append(cnt)

    return answer

print(solution([95, 90, 99, 99, 80, 99],[1, 1, 1, 1, 1, 1]))