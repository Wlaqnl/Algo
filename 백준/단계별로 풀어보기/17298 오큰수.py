import sys
sys.stdin=open('17298 오큰수.txt',"r")
T=int(input())

for tc in range(T):
    # pypy도 시간초과
    # n=int(input())
    # num=list(map(int,input().split()))
    # ans=[]
    #
    # for i in range(n):
    #     if max(num)==num[i] or i==n-1:
    #         ans.append(-1)
    #     else:
    #         for j in range(i+1,n):
    #             if num[i]<num[j]:
    #                 ans.append(num[j])
    #                 break
    #             elif num[i]==max(num[i:]):
    #                 ans.append(num[i])
    # print(' '.join(map(str,ans)))

    # stack 이용! 이것도 시간초과
    # n=int(input())
    # num=list(map(int,input().split()))
    # stack=[]
    # ans=[]
    # cnt=0
    # maxV=num[0]
    # a=max(num)
    #
    # while num:
    #     stack.append(num.pop(0))
    #     if a != maxV:
    #         if stack[-1]>maxV:
    #             ans.append(stack[-1])
    #             maxV=stack[-1]
    #             cnt+=1
    #     else:
    #         if not ans:
    #             ans.append(-1)
    #             cnt+=1
    #
    # while len(ans)!=n:
    #     if cnt<n-1:
    #         ans.append(max(stack[cnt:]))
    #         cnt+=1
    #     else:
    #         ans.append(-1)
    #
    # print(' '.join(map(str,ans)))

    #참고 https://hooongs.tistory.com/329
    N=int(input())
    num=list(map(int,input().split()))

    stack=[]
    result = [-1 for _ in range(N)]

    stack.append(0)
    i=1

    while stack and i<N:
        while stack and num[stack[-1]]<num[i]:
            result[stack[-1]]=num[i]
            stack.pop()

        stack.append(i)
        i+=1

    for i in result:
        print(i, end=' ')

