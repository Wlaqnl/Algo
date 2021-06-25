import sys
sys.stdin=open("1316 그룹 단어 체커.txt","r")
T=int(input())
ans=0

for tc in range(T):
    check=[0]*26
    word=input()

    for i in range(len(word)):
        if check[ord(word[i])-97]==0:
            check[ord(word[i]) - 97]+=1
            cnt=1
        else:
            if i>=1:
                if word[i-1]==word[i]:
                    continue
                else:
                    break
    else:
        ans+=1
print(ans)
