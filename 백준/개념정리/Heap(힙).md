### Heap(힙)

---

**완전 이진 트리**

* 노드가 올라갈수록 데이터의 값이 높은 힙 : 최대 힙
* 노드가 올라갈수록 데이터의 값이 낮은 힙 : 최소 힙





### 우선 순위 큐

---

**우선 순위가 가장 높은 자료를 가장 먼저 꺼낼 수 있는 자료 구조**

> import heapq

1. 우선 순위 큐의 생성 및 원소 삽입
   * heapq.heappush(리스트, (우선순위 값, 넣을 데이터)) -> O(NlogN)
2. 원소 꺼내기
   * heapq.heappop() -> 우선순위 빠른 순서대로 나옴 O(logN)
3. 배열로 힙 정렬 만들기
   * heapq.heapify(리스트) -> O(N)

4. heapq는 최소 힙 밖에 지원 안한다.