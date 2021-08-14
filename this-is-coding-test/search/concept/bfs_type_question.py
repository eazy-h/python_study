from collections import deque


# 너비 우선 탐색 (가까운 노드를 우선 탐색)
# 선입선출 큐 자료구조 사용 (dfs는 후입선출 - 스택 자료구조 사용)
# O(N) 시간
# 일반적으로 실제 수행시간은 DFS보다 좋은 편 (예외 있음)


def bfs_func(graph, start, visited):
    # 큐 사용 라이브러리
    queue = deque([start])  # 말 그대로 queue[0] = 1

    # 현 노드 방문
    visited[start] = True

    while queue:  # 큐가 존재할때만 반복
        v = queue.popleft()  # 첫번째 원소 뽑기
        print(v, end=" ")
        for i in graph[v]:  # graph 1번 노드부터 돌기
            if not visited[i]:  # 처음엔 다 False니 접근
                queue.append(i) # Queue에 추가 ex) 1번 노드에 너비 우선 [2,3,8] 노드 추가
                visited[i] = True


bfs_graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

visited = [False] * 9
bfs_func(bfs_graph, 1, visited)
