import sys
sys.stdin = open("1이 될 때까지.txt","r")

N, K = map(int,input().split())
result = 0

while N>=K:
    #N이 K로 나누어 떨어지지 않는다면 N에서 1씩 빼기
    while N%K!=0:
        N-=1
        result+=1
    N//=K
    result+=1

while N>1:
    N-=1
    result+=1

print(result)