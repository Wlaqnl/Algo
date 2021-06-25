import sys
sys.stdin=open("1011 Fly me to the Alpha Centauri.txt","r")

T = int(input())
for i in range(T):
    # start, end = map(int, input().split())
    # between = end - start
    # flag = 0
    # num = 1
    # while between > 0:
    #
    #     if flag % 2 == 1:
    #         between -= num
    #         num += 1
    #         flag += 1
    #     else:
    #         between -= num
    #         flag += 1
    # print(flag)
    s, e = map(int,input().split())
    goal = e - s
    bal = 0
    dari = 0

    while True:
        dari += 1
        bal += dari * 2
        if goal <= (bal - dari):
            print(dari * 2 - 1)
            break
        elif goal <= bal:
            print(dari * 2)
            break