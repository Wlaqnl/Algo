import sys
sys.stdin=open("문자열 재정렬.txt","r")
T=int(input())

for tc in range(T):
    text=input()
    value=0
    string=''

    for i in sorted(text):
        if i.isdigit():
            value+=int(i)
        else:
            string+=i

    if value:
        print(string+str(value))
    else:
        print(string)