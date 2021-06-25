> ### Lv.1 모의고사

---

```python
def solution(answers):
    ans=[]
    stu1=[1,2,3,4,5]
    stu2=[2,1,2,3,2,4,2,5]
    stu3=[3,3,1,1,2,2,4,4,5,5]
    N=len(answers)
    point=[0]*3

    for n in range(N):
        if n>=len(stu1):
            if answers[n]==stu1[n%len(stu1)]:
                point[0]+=1
        else:
            if answers[n]==stu1[n]:
                point[0]+=1

        if n>=len(stu2):
            if answers[n]==stu2[n%len(stu2)]:
                point[1]+=1
        else:
            if answers[n]==stu2[n]:
                point[1]+=1

        if n>=len(stu3):
            if answers[n]==stu3[n%len(stu3)]:
                point[2]+=1
        else:
            if answers[n]==stu3[n]:
                point[2]+=1
    m=max(point)

    for p in range(len(point)):
        if point[p]==m:
            ans.append(p+1)

    return ans

print(solution([1,2,3,4,5,1,2,3,4,5]))
print(solution([1,2,3,4,5]))
print(solution([1,3,2,4,2]))

```

