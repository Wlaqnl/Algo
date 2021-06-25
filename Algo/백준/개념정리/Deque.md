### deque

---

> #### 사용법 => 기본 정의 무조건 하고 후에 작업을 실행해야함

```python
from collections import deque
이름 = deque([리스트]) 
```



* 오른쪽 삽입

```python
이름.append(삽입할 것)
```



* 왼쪽 삽입

```python
이름.appendleft(삽입할 것)
```



* 모든 요소 제거

```python
이름.clear()
```



* i번째 index에 x를 삽입

```python
이름.insert(i, 'x')
```



* 맨 오른쪽 요소 제거

```python
저장할 이름 = 이름.pop()
```



* 왼쪽 요소 제거

```python
저장할 이름 = 이름.popleft()
```

