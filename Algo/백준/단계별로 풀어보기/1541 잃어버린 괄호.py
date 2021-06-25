import sys
sys.stdin=open("1541 잃어버린 괄호.txt")

#최소값을 만들기 위해 -기준으로 괄호를 치고
#맨 처음 원소는 더해주고 나머지는 빼준다.
exp=input().split('-')
num=[]

for e in exp:
    cnt=0
    s=e.split('+')
    for j in s:
        cnt+=int(j)
    num.append(cnt)
n=num[0]

for i in range(1,len(num)):
    n-=num[i]
print(n)
