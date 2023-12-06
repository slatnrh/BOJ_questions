from collections import deque
import sys
input = sys.stdin.readline

# bfs: 시작점을 기준으로 연결된 노드를 탐색하며 방문한 노드의 수(케빈 베이컨 수)를 세는 함수
def bfs(start):
    # (노드, 케빈 베이컨 수)의 튜플로 큐에 저장
    queue = deque([(start, 0)])
    visited = [False] * (N+1)
    visited[start] = True
    # 케빈 베이컨 수를 합산할 변수
    kevin_bacon_sum = 0

    while queue:
        current_node, bacon_number = queue.popleft()
        # 케빈 베이컨 수 누적
        kevin_bacon_sum += bacon_number

        for adjacent_node in graph[current_node]:
            if not visited[adjacent_node]:
                visited[adjacent_node] = True
                # 인접 노드와의 케빈 베이컨 수 증가
                queue.append((adjacent_node, bacon_number + 1))

    return kevin_bacon_sum


N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

# 최소 케빈 베이컨 수를 무한대로 초기화
min_kevin_bacon = float('inf')
kevin_bacon_lst = []

for node in range(1, N+1):
    kevin_bacon = bfs(node)
    # 최소 케빈 베이컨 수 갱신
    min_kevin_bacon = min(min_kevin_bacon, kevin_bacon)
    # 노드별 케빈 베이컨 수 append
    kevin_bacon_lst.append(min_kevin_bacon)

# 최소 케빈 베이컨 수의 인덱스 출력
print(kevin_bacon_lst.index(min(kevin_bacon_lst))+1)