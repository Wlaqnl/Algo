def solution(numbers):
    numbers = list(map(str,numbers)) #numbers안에 모든 요소를 str형태로 바꾼후 다시 list로 저장
    numbers.sort(key=lambda x: x * 3, reverse=True) #1000이하의 수니깐 3자리수까지 맞춰줌
    if sum(list(map(int,numbers))) == 0: #만약 numbers의 모든수의 합이 0이면
    	numbers = list(set(numbers)) #numbers에 set(numbers)를 대입
    return "".join(numbers) #이어붙인 수를 출력

print(solution([6, 10, 2]))