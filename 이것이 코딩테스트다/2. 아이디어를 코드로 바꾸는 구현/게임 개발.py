import sys
sys.stdin=open("게임 개발.txt","r")

N, M = map(int,input().split())

d=[[0]*M for _ in range(N)]

x, y, direction = map(int,input().split())
d[x][y]=1

array=[]
for i in range(N):
    array.append(list(map(int,input().split())))

dx=[-1,0,1,0]
dy=[0,1,0,-1]

# 왼쪽으로 회전
def turn_left():
    global direction
    direction-=1
    if direction == -1:
        direction=3

# 시뮬레이션 시작
count=1
turn_time=0
while True:
    turn_left()
    nx = x+dx[direction]
    ny = y+dy[direction]

    if d[nx][ny] == 0 and array[nx][ny]==0:
        d[nx][ny]=1
        x=nx
        y=ny
        count+=1
        turn_time=0
        continue
    else:
        turn_time+=1

    if turn_time==4:
        nx = x-dx[direction]
        ny = y-dy[direction]

        if array[nx][ny]==0:
            x=nx
            y=ny

        else:
            break
        turn_time=0

print(count)