from collections import deque

# 깊이 우선 탐색 (깊은 부분을 우선적 탐색)
# 스택 자료구조(재귀)를 이용한다.
# 1. 시작 노드 스택을 삽입, 방문
# 2. 스택에 최상단 노드 방문하지 않은 인접노드를 스택에 넣고 방문처리, 방문하지 않은 인접노드가 없을시 스택에서 최상단 노드를 꺼냄 (스택은 LIFO)
# 3. 2번이 수행할 수 없을때까지 반복

stack = []

stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop()
stack.append(1)
stack.append(4)
stack.pop()

print(stack)  # 5,2,3,1
print(stack[::-1])  # 최상단 노드부터 출력 (reverse와 같은 의미)

# 큐는 선입선출
# 큐 구현시 deque 사용하기 데이터 빼고 삽입하는데 리스트에 비해 빠르고 효율적이다.

queue = deque()

queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()

print(queue)  # 3,7,1,4
queue.reverse()  # 반대로
print(queue)  # 4,1,7,3
