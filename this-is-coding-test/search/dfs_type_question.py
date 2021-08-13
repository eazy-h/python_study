from collections import deque

# 깊이 우선 탐색 (깊은 노드를 우선 탐색)
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

# print(stack)  # 5,2,3,1
# print(stack[::-1])  # 최상단 노드부터 출력 (reverse와 같은 의미)

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

# print(queue)  # 3,7,1,4
# queue.reverse()  # 반대로
# print(queue)  # 4,1,7,3


# 인접 행렬 방식 예제
# 모든 "관계"를 저장하기에 불필요한 메모리 낭비
matrix_graph = [
    [0, 7, 5],  # 0번 노드의 각 연결된 노드 정보 [0번노드, 1번노드, 2번노드]
    [7, 0, 999999999],
    [5, 999999999, 0],
]

# 인접리스트 방식 예제
# 모든 노드에 연결된 노드에 대한 정보를 차례대로 연결
graph = [[] for _ in range(3)]
print(graph)

# 각 노드에 연결된 정보 저장(노드, 간선거리)
graph[0].append((1, 7))  # 노드 0번에 연결된 노드 정보 저장 (노드, 거리)
graph[0].append((2, 5))  # 노드 0번에 연결된 노드 정보 저장 (노드, 거리)
graph[1].append((0, 7))  # 노드 1번에 연결된 노드 정보 저장 (노드, 거리)
graph[2].append((0, 5))  # 노드 2번에 연결된 노드 정보 저장 (노드, 거리)

print(graph[0])

# "행렬방식"은 특정 두 노드가 "연결되어 있는지 확인"하기 더 유리 [0][7] -> 0번노드와 7번노드를 뜻함
# 연결리스트는 차례대로 순차적으로 확인해야하기에 이때는 비효율적 (모든 노드를 순회하는 경우 더 효과적)


dfs_graph = [
    [],  # 1번 노드부터 시작
    [2, 3, 8],  # 1번 노드에서 접근 가능한 노드 나열
    [1, 7],  # 2번 노드에서 접근 가능한 노드 나열
    [1, 4, 5],  # 3번 노드에서 접근 가능한 노드 나열
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]  # ...8번
]


# 대망의 DFS 코드
def dfs_func(graph, v, visited):  # (그래프, 시작 노드, 방문처리할 배열  default false)
    # 현재 바라보는 노드 방문처리
    visited[v] = True
    print(v, end=" ")

    # 현 노드에 연결된 다른 노드에 재귀를 사용하여 접근
    for i in graph[v]:  # 9번을 반복 (처음 1번 노드에서 접근 가능한 [2,3,8] 노드를 반복해서 3번 방문 -> 약간 2중 for문이라 생각하면 비슷?)
        if not visited[i]:  # False일때 다시 재접근
            dfs_func(graph, i, visited)


visited = [False] * 9
dfs_func(dfs_graph, 1, visited)
