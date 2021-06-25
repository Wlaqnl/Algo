d=[0]*100

def fibo(x):
    print('f('+str(x)+')', end=' ') #어떤 함수 호출했는지 알 수 있음
    if x==1 or x==2:
        return 1
    if d[x]!=0:
        return d[x]
    d[x]=fibo(x-1)+fibo(x-2)
    return d[x]

print(fibo(99))