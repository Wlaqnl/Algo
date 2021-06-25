import sys,math
sys.stdin=open("9020 골드바흐의 추측.txt","r")

array = [True for i in range(10001)]
array[1] = 0

for i in range(2, int(math.sqrt(10000)) + 1):
    if array[i] == True:
        j = 2
        while i * j <= 10000:
            array[i * j] = False
            j += 1

T=int(input())

for tc in range(T):
    n=int(input())
    #dist=1e9

    # for k in range(2,n//2+1):
    #     if array[k]==True and array[n-k]==True:
    #         if dist>n-k-k:
    #             dist=n-k-k
    #             a=k
    #             b=n-k

    #거꾸로 찾는 것이 훨씬 더 효율적 ( 무려 4배나! )
    for k in range(n//2,1,-1):
        if array[k]==True and array[n-k]==True:
            print(k,n-k)
            break


