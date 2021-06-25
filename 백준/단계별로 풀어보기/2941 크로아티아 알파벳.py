import sys
sys.stdin=open("2941 크로아티아 알파벳.txt","r")
T=int(input())

for tc in range(T):
    croatia=input()
    shift=['c=','c-','dz=','d-','lj','nj','s=','z=']

    for s in shift:
        if s in croatia:
            croatia=croatia.replace(s," ")
    print(len(croatia))
