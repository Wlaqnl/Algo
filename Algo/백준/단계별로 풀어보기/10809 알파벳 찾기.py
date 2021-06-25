import sys
sys.stdin=open("10809 알파벳 찾기.txt","r")

word=input()
check=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
ans=[]

for c in check:
    if c in word:
        ans.append(word.index(c))
    else:
        ans.append(-1)
print(' '.join(map(str,ans)))