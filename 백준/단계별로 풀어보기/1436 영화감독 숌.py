import sys
sys.stdin=open("1436 영화감독 숌.txt","r")

n=int(input())
movie=666
cnt=0
while True:
    if '666' in str(movie):
        cnt+=1
        if cnt==n:print(movie);break
    movie+=1
