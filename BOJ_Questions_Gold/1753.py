import heapq, sys
input = sys.stdin.readline

def dijkstra(graph, start):
    # 다익스트라(dijkstra): 자신을 제외한 (자신은 0) 모든 노드 간의 거리를 inf로 설정
    distances = [float('inf')] * (V + 1)
    distances[start] = 0
    # 방문 여부 저장
    visited = [False] * (V + 1)
    # queue에 (거리, 노드)를 저장
    queue = [(0, start)]

    while queue:
        # 현재 거리, 노드를 각각 할당
        current_distance, current_node = heapq.heappop(queue)

        # 방문했다면 continue
        if visited[current_node]:
            continue
        
        # 방문 여부 표시
        visited[current_node] = True

        for adjacent, weight in graph[current_node]:
            # 저장된 노드 + 현재 거리
            distance = current_distance + weight

            # 이때 거리가 저장된 노드의 거리보다 작다면 저장
            if distance < distances[adjacent]:
                distances[adjacent] = distance
                heapq.heappush(queue, (distance, adjacent))

    # 시작점으로부터 각 지점들 간의 최단거리 return
    return distances

V, E = map(int, input().split())
K = int(input())

graph = [[] for _ in range(V + 1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

# 최단거리만 가져가기 위해 [1:]
dijkstra_lst = dijkstra(graph, K)[1:]

for value in dijkstra_lst:
    print(value if value != float('inf') else "INF")
