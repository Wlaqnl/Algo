import sys,math
sys.stdin=open("3053 택시 기하학.txt","r")
T=int(input())

for tc in range(T):
    r=int(input())
    print(round(math.pi*r*r,6))
    print(f'{r*r*2:.6f}')