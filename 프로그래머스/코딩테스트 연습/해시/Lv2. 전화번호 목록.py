def solution(phone_book):
    answer=True
    num=sorted(phone_book)
    Flag=True

    for i in range(len(num)-1):
        if Flag:
            for j in range(i+1,len(num)):
                if num[i] == num[j][:len(num[i])]:
                    answer=False
                    Flag=False
                    break

    return answer
print(solution(["119", "97674223", "1195524421"]))