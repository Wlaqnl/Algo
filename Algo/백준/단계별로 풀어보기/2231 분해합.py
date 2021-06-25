import sys
sys.stdin=open("2231 분해합.txt","r")

# N=int(input())
#
# for i in range(1, N):
#     ans=i
#     num=i
#     while i>=10:
#         num+=i%10
#         i=i//10
#     num+=i
#     if num==N:
#         print(ans)
#         break
# else:
#     print(0)

num = int(input())
answer = 0

for i in range(1, num + 1):
    coef_num_list = list(map(int, str(i)))
    answer = i + sum(coef_num_list)

    if answer == num:
        print(i)
        break

    if i == num:
        print(0)