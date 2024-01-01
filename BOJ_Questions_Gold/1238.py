import heapq, sys
from collections import defaultdict
input = sys.stdin.readline
INF = int(1e9)

def dijkstra(start):
    q = []
    # 다익스트라(dijkstra): 자신을 제외한 (자신은 0) 모든 노드 간의 거리를 inf로 설정
    distances = [INF] * (N + 1)
    distances[start] = 0
    # queue에 (거리, 노드)를 저장
    heapq.heappush(q, (0, start))

    while q:
        # 현재 거리, 노드를 각각 할당
        current_distance, current_node = heapq.heappop(q)

        if distances[current_node] < current_distance:
            continue

        for adjacent, weight in graph[current_node]:
            # 저장된 노드 + 현재 거리
            distance = current_distance + weight

            # 이때 거리가 저장된 노드의 거리보다 작다면 저장
            if distance < distances[adjacent]:
                distances[adjacent] = distance
                heapq.heappush(q, (distance, adjacent))

    # 시작점으로부터 각 지점들 간의 최단거리 return
    return distances


N, M, X = map(int, input().split())

graph = [[] for _ in range(N + 1)]

for _ in range(M):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

max_time = 0

for i in range(1, N + 1):
    go = dijkstra(i)
    back = dijkstra(X)
    max_time = max(max_time, go[X] + back[i])

print(max_time)