import sys, time
sys.stdin=open("큰 수의 법칙.txt","r")


start_time = time.time()
n, m, k = map(int,input().split())
num=list(map(int,input().split()))

#큰 수 찾을 때 바로 sort함수 실행
num.sort()

first = num.pop(-1)
second = num.pop(-1)

result=0

while True:
    for i in range(k):
        if m==0:
            break
        result+=first
        m-=1

    if m==0:
        break
    result+=second
    m-=1

end_time = time.time()


print(result)
