from collections import deque
import heapq, sys
input = sys.stdin.readline

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    queue = [(0, start)]

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        if current_distance > distances[current_node]:
            continue

        for adjacent, weight in graph[current_node].items():
            distance = current_distance + weight

            if distance < distances[adjacent]:
                distances[adjacent] = distance
                heapq.heappush(queue, (distance, adjacent))

    return distances

N, E = map(int, input().split())
graph = {i: {} for i in range(1, N + 1)}

for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a][b] = c
    graph[b][a] = c

v1, v2 = map(int, input().split())

# 각 지점에서 다른 지점까지의 최단 거리 계산
dist_from_start = dijkstra(graph, 1)
dist_from_v1 = dijkstra(graph, v1)
dist_from_v2 = dijkstra(graph, v2)

# 경우의 수에 따른 최단 경로 계산(min 첫번째 인자: v1을 먼저 거칠 때의 거리, min 두번째 인자: v2를 먼저 거칠 때의 거리)
result = min(dist_from_start[v1] + dist_from_v1[v2] + dist_from_v2[N], dist_from_start[v2] + dist_from_v2[v1] + dist_from_v1[N])

# 그러한 경로가 없을 때 -1 출력
if result >= float('inf'):
    print(-1)
else:
    print(result)