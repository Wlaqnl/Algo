import sys
sys.stdin = open("1이 될 때까지.txt","r")

N, K = map(int,input().split())
result = 0

while True:
    # (N==K 로 나누어 떨어지는 수가 될 때까지 1씩 빼기)
    target=(N//K)*K
    result+=(N-target)
    N=target
    if N<K:
        break
    result+=1
    N//=K

result+=(N-1)
print(result)