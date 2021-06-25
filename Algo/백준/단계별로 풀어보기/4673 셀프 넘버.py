check = [1] + [0] * 10000
ans=[]

def self_num(check, num):
    while num<10000:
        copy_num=num
        value=copy_num
        while copy_num>=10:
            value+=copy_num%10
            copy_num=copy_num//10
        value+=copy_num
        if value<=10000 and check[value]==0:
            check[value]=1
        num=value
    return

while check.count(1)<10001:
    #print(check.index(0))
    k=check.index(0)
    ans.append(k)
    check[k]+=1
    self_num(check, k)

for i in ans:
    print(i)


