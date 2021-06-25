import sys
sys.stdin=open("2775 부녀회장이 될테야.txt","r")
T=int(input())

for tc in range(T):
    floor = int(input())
    ho = int(input())
    people=[i for i in range(1, ho+1)]
    #print(people)

    for x in range(floor):
        for y in range(1, ho):
            people[y]+=people[y-1]
    print(people[-1])





