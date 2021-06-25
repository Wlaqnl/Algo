import sys
sys.stdin=open("1157 단어 공부.txt","r")
T=int(input())

for tc in range(T):
    word=input().upper()
    check=[0]*26
    # print(ord("A"))
    max_value=-1
    max_cnt=0

    for w in word:
        check[ord(w)-65]+=1

    for i in check:
        if max_value<i:
            max_value=i
            max_cnt=1
            ans=check.index(i)
        elif max_value==i:
            max_cnt+=1
    if max_cnt>1:
        print("?")
    else:
        print(chr(ans+65))