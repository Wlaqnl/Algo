import sys
sys.stdin=open("2629 양팔저울.txt","r")

N=int(input())
weight=list(map(int,input().split()))

M=int(input())
check=list(map(int,input().split()))

visited = [True] + [False] * (sum(weight))

for c in weight:
    # visited 쓰는 경우
    # IndexError: list index out of range
    # i = 무게 / e = 체크 여부
    for i, e in enumerate(visited[:]):
        # 해당 무게가 체크 된 경우
        if e:
            # 해당 무게 + 추가 추 부분 체크
            if not (visited[i+c]):
                visited[i+c] = True


for c in weight:
    for i, e in enumerate(visited[:]):
        #print(i,e)
        if e:
            # 양수인 부분 중에
            if i-c >= 0:
                # 해당 무게 - 추가 추 부분 체크
                if not(visited[i-c]):
                    visited[i-c] = True

for c in check:
    # 측정하고자하는 추무게가 주어진 총 무게보다 큰경우
    if c > len(visited) - 1:
        print('N', end=' ')
    else:
        if visited[c]:
            print('Y', end=' ')
        else:
            print('N', end=' ')



