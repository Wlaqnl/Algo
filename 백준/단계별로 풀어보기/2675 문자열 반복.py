import sys
sys.stdin=open("2675 문자열 반복.txt","r")
T=int(input())

for tc in range(T):
    repeat, word=input().split()
    ans=''
    for i in word:
        ans+=i*int(repeat)
    print(ans)