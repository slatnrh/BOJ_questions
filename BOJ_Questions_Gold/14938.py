import sys, heapq
input = sys.stdin.readline
INF = int(1e9)

# dijkstra: 각 시작 노드에서부터 각 정점까지의 최소거리 저장
def dijkstra(graph, start, search_range, items):
    distances = [INF] * (n + 1)
    distances[start] = 0
    queue = []
    heapq.heappush(queue, (0, start))

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        if distances[current_node] < current_distance:
            continue
        
        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))
    
    return distances

n, m, r = map(int, input().split())
t = list(map(int, input().split()))

graph = [[] for _ in range(n + 1)]
for i in range(r):
    a, b, l = map(int, input().split())
    graph[a].append((b, l))
    graph[b].append((a, l))

# 거리를 비교하가며 아이템 개수 저장
result = 0
for start in range(1, n + 1):
    collected = dijkstra(graph, start, m, t[:n])
    temp = 0
    for i, d in enumerate(collected[1:]):
        if d <= m:
            temp += t[i]
    if temp > result:
        result = temp

print(result)