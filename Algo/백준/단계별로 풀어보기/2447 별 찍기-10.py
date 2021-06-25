import sys
sys.stdin=open("2447 별 찍기-10.txt","r")

# # 별 찍는 재귀 함수
# def draw_star(n):
#     global Map
#
#     if n == 3:
#         Map[0][:3] = Map[2][:3] = [1] * 3
#         Map[1][:3] = [1, 0, 1]
#         return
#
#     a = n // 3
#     draw_star(n // 3)
#     for i in range(3):
#         for j in range(3):
#             if i == 1 and j == 1:
#                 continue
#             for k in range(a):
#                 Map[a * i + k][a * j:a * (j + 1)] = Map[k][:a]  # 핵심 아이디어
#
#
# N = int(input())
#
# # 메인 데이터 선언
# Map = [[0 for i in range(N)] for i in range(N)]
#
# draw_star(N)

# for i in Map:
#     for j in i:
#         if j:
#             print('*', end='')
#         else:
#             print(' ', end='')
#     print()

def get_stars(n):
    matrix = []
    for i in range(3 * len(n)):
        if i // len(n) == 1:
            matrix.append(n[i % len(n)] + " " * len(n) + n[i % len(n)])
        else:
            matrix.append(n[i % len(n)] * 3)
    return matrix


star = ["***", "* *", "***"]
n = int(input())
e = 0
while n != 3:
    n = int(n / 3)
    e += 1

for i in range(e):
    star = get_stars(star)
for i in star:
    print(i)
