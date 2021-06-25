from math import factorial
import sys
sys.stdin=open("2004 조합 0의 개수.txt","r")

#https://somjang.tistory.com/entry/BaeKJoon-2004%EB%B2%88-%EC%A1%B0%ED%95%A9-0%EC%9D%98-%EA%B0%9C%EC%88%98-Python
# 시간초과 남
# n, m = map(int,input().split())
# num=str(factorial(n)//(factorial(m)*factorial(n-m)))
# a=len(num)
# cnt=0
# #print(num)
#
# for i in range(a-1,-1,-1):
#     if num[i]=='0':
#         cnt+=1
#     else:
#         print(cnt)
#         break

# 블로그 코드 참고
def div_number(k, n):
    count = 0
    while(k != 0):
        k = k // n
        count += k
    return count

n, m = list(map(int, input().split()))

div_five = div_number(n, 5) - div_number(m, 5) - div_number(n-m, 5)
div_two = div_number(n, 2) - div_number(m, 2) - div_number(n-m, 2)

print(min(div_five, div_two))