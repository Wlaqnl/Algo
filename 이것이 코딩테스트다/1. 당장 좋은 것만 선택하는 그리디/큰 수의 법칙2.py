import sys, time
sys.stdin=open("큰 수의 법칙.txt","r")


start_time = time.time()
n, m, k = map(int,input().split())
num = list(map(int,input().split()))

num.sort()
first = num.pop(-1)
second = num.pop(-1)

count = int(m/(k+1))*k
count+= m%(k+1)

result=0
result+=(count)*first
result+=(m-count)*second

end_time = time.time()

print(result)
print(end_time-start_time)

