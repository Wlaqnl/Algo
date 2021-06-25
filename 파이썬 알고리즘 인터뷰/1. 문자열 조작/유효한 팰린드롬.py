#1. 리스트로 변환
def isPalindrome(s):
    strs = []
    for char in s:
        if char.isalnum():
            strs.append(char.lower())
    # print(strs)

    while len(strs) > 1:
        if strs.pop(0) != strs.pop():
            return False

    return True

#2. 데크 자료형을 이용한 최적화
import collections
def isPalindrome(s):
    strs=collections.deque()

    for char in s:
        if char.isalnum():
            strs.append(char.lower())

    while len(strs) > 1:
        if strs.popleft() != strs.pop():
            return False

    return True

#3. 슬라이싱 사용
import re
def isPalindrome(s):
    s = s.lower()
    s = re.sub('[^a-z0-9]', '', s)

    return s == s[::-1]
print(isPalindrome("A man, a plan, a canal: Panama"))
print(isPalindrome("race a car"))