import sys
sys.stdin=open("문자열 재정렬.txt","r")
T=int(input())

for tc in range(T):
    data=input()
    result=[]
    value=0

    for x in data:
        if x.isalpha():
            result.append(x)
        else:
            value+=int(x)

    result.sort()

    if value!=0:
        result.append(str(value))

    print(''.join(result))