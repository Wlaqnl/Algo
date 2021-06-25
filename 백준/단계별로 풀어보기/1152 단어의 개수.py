import sys
sys.stdin=open("1152 단어의 개수.txt","r")
T=int(input())

for tc in range(T):
    words=input()

    if words[0]==" ":
        ans=0
    else:
        ans=1

    for i in range(len(words)-1):
        if words[i]==" " and words[i+1]!=" ":
            ans+=1
    print(ans)