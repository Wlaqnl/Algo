import sys
sys.stdin=open("5622 다이얼.txt","r")

dial={'ABC':2,'DEF':3,'GHI':4,'JKL':5,'MNO':6,'PQRS':7, 'TUV':8, 'WXYZ':9}

char=input()
ans=0

for i in char:
    for j in dial.keys():
        if i in j:
            ans+=dial.get(j)+1
print(ans)