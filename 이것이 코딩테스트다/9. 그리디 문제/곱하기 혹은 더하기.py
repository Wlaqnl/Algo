import sys
sys.stdin=open("곱하기 혹은 더하기.txt","r")

T=int(input())

def cal(arr, idx, value, sign):
    global maxV
    if idx==len(arr)-1:
        if value>maxV:
            maxV=value
        return

    else:
        if sign==1:
            cal(arr, idx+1, value+arr[idx+1], 1)
            cal(arr, idx+1, value+arr[idx+1], 2)


        else:
            cal(arr, idx + 1, value * arr[idx + 1], 1)
            cal(arr, idx + 1, value * arr[idx + 1], 2)


for i in range(T):
    data=input()
    num=[]
    maxV=0
    for d in data:
        num.append(int(d))
    #print(num)

    cal(num, 0, num[0], 1)
    cal(num, 0, num[0], 2)
    print(maxV)
