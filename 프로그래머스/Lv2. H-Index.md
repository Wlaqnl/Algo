### Lv2. H-Index

---

```python
def solution(citations):
    answer=0
    citations.sort()
    #print(citations)
    max_citations=max(citations)
    idx_citations=len(citations)-1
    stop=True

    for i in range(max_citations, -1, -1):
        if i in citations:
            idx_citations=citations.index(i)
            if len(citations)-idx_citations>=i and idx_citations<=i:
                answer=i
                break
        else:
            while citations[idx_citations]>i and stop:
                if idx_citations>0:
                    idx_citations-=1
                else:
                    answer=len(citations)
                    stop=False

            if len(citations)-idx_citations-1>=i and idx_citations<=i and stop:
                answer=i
                break

    return answer
```

* `idx_citations<=i` 조건 생략 가능