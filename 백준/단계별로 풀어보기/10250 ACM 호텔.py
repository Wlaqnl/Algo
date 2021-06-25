import sys
sys.stdin=open("10250 ACM 호텔.txt","r")
# T=int(input())
#
# for tc in range(T):
#     H, W, N = map(int,input().split())
#     if N%H:
#         ROOM=str(N%H)
#         if len(str(N // H + 1)) == 1:
#             ROOM += '0' + str(N // H + 1)
#         else:
#             ROOM += str(N // H + 1)
#
#     else:
#         ROOM=str(H)
#         if  len(str(N//H))==1:
#             ROOM+='0'+str(N//H)
#         else:
#             ROOM+=str(N//H)
#
#     print(ROOM)

t = int(input())

for i in range(t):
    h, w, n = map(int, input().split())
    num = n//h + 1
    floor = n % h
    if n % h == 0:  # h의 배수이면,
        num = n//h
        floor = h
    print(f'{floor*100+num}')