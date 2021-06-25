from collections import deque
import sys
sys.stdin=open('2164 카드2.txt',"r")

n=int(input())
card=deque()

for i in range(n):
    card.append(n-i)
#print(card)

while len(card)>1:
    card.pop()
    card.appendleft(card.pop())
print(card[0])