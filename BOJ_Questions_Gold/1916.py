import heapq, sys
input = sys.stdin.readline

def dijkstra(graph, start, end):
    # 다익스트라(dijkstra): 자신을 제외한 (자신은 0) 모든 노드 간의 거리를 inf로 설정
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    # queue에 (거리, 노드)를 저장
    queue = [(0, start)]

    while queue:
        # 현재 거리, 노드를 각각 할당
        current_distance, current_node = heapq.heappop(queue)

        # 현재 거리(current_distance)가 저장된 노드의 거리(distances[current_node])보다 크다면 넘어가기
        if current_distance > distances[current_node]:
            continue
        
        for adjacent, weight in graph[current_node].items():
            # 저장된 노드 + 현재 거리
            distance = current_distance + weight

            # 이때 거리가 저장된 노드의 거리보다 작다면 저장
            if distance < distances[adjacent]:
                distances[adjacent] = distance
                heapq.heappush(queue, (distance, adjacent))

    # 종점까지의 거리(최솟값)을 return
    return distances[end]

N = int(input())
M = int(input())

graph = {i: {} for i in range(1, N + 1)}

for _ in range(M):
    u, v, w = map(int, input().split())
    if v in graph[u]:
        graph[u][v] = min(graph[u][v], w)
    else:
        graph[u][v] = w

start, end = map(int, input().split())

result = dijkstra(graph, start, end)
print(result)