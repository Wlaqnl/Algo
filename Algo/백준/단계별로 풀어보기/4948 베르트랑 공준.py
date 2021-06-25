import sys,math
sys.stdin=open("4948 베르트랑 공준.txt","r")

num=[]
while True:
    n=int(input())
    if n==0:
        break
    else:
        num.append(n)

array = [True for i in range(246913)]
array[1] = 0

for i in range(2,int(math.sqrt(246912))+1):
    if array[i]==True:
        j=2
        while i*j<=2*123456:
            array[i*j]=False
            j+=1
    #print(array)

for n in num:
    cnt=0
    for k in range(n+1, 2*n+1):
        if array[k]==True:
            cnt+=1
    print(cnt)
