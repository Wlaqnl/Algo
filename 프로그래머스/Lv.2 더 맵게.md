### Lv.2 더 맵게

---

```python
import heapq

def solution(scoville, K):
    answer=0
    heapq.heapify(scoville)
    #print(scoville)
    mix=True

    while mix:
        a=heapq.heappop(scoville)
        if len(scoville):
            b = heapq.heappop(scoville)
        else:
            return -1

        heapq.heappush(scoville,a+b*2)
        answer+=1

        if scoville[0]>K:
            mix=False

    return answer

```

