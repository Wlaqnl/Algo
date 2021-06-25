import sys
sys.stdin=open("1427 소트인사이드.txt","r")

N=int(input())
ans=sorted(list(str(N)), reverse=True)
print(''.join(ans))
