#1. 리스트 변환
from typing import List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def isPalindrome(head: ListNode):
    q: List = []

    if not head:
        return True

    node = head
    # 리스트 변환
    while node is not None:
        q.append(node.val)
        node = node.next

    # 팰린드롬 판별
    while len(q) > 1:
        if q.pop(0) != q.pop():
            return False

    return True

#2. 데크를 이용한 최적화
#(1번 방법은 O(n)이 발생하지만 데크는 O(1)이 발생)
import collections
from typing import Deque

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def isPalindrome(head: ListNode):
    # 데크 자료형 선언
    q: Deque = collections.deque()

    if not head:
        return True

    node = head
    while node is not None:
        q.append(node.val)
        node = node.next

    while len(q) > 1:
        if q.popleft() != q.pop():
            return False

    return True

#3. 런너를 이용한 우아한 풀이
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def isPalindrome(head: ListNode):
    rev = None
    slow = fast = head
    # 런너를 이용해 역순 연결 리스트 구성
    while fast and fast.next:
        fast = fast.next.next
        rev, rev.next, slow = slow, rev, slow.next
    if fast:
        slow = slow.next

    # 팰린드롬 여부 확인
    while rev and rev.val == slow.val:
        slow, rev = slow.next, rev.next
    return not rev

print(isPalindrome([1,2])) #실행 안됨
print(isPalindrome([1,2,2,1])) #실행 안됨