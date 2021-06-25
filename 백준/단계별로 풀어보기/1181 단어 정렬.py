import sys
sys.stdin=open("1181 단어 정렬.txt","r")

N=int(input())
word=[]

for _ in range(N):
    w=input()
    word.append((w,len(w)))
#print(word)
words=sorted(word, key=lambda x:(x[1],x[0]))
#print(words)
ans=[]

for i in words:
    a, b = i[0],i[1]
    if not a in ans:
        ans.append(a)
        print(a)
    else:
        continue