import sys
sys.stdin=open("9012 괄호.txt","r")
T=int(input())

for tc in range(T):
    n=int(input())

    for _ in range(n):
        bracket=list(input())
        #print(bracket)
        s=[]

        for b in bracket:
            if b=='(':
                s.append(b)
            else:
                if s:
                    s.pop()
                else:
                    print('NO')
                    break
        else:
            if s:
                print('NO')
            else:
                print('YES')