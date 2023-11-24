from collections import deque
import sys
input = sys.stdin.readline

# bfs: 간선으로 연결된 모든 점 visited 리스트에 저장해서 한 선에 어느 점들이 연결되어 있는 지 확인
def bfs(start):
    queue = deque([start])
    # visited 점은 True로 변환하여 연결 확인
    visited[start] = True

    while queue:
        # x에 탐색할 점 저장
        x = queue.popleft()
        for i in graph[x]:
            # 방문 안 한 점이 있다면
            if not visited[i]:
                # 그 점 True로 변환
                visited[i] = True
                # 다시 queue에 저장하여 재탐색
                queue.append(i)

N, M = map(int, input().split())
# 각 점들이 어느 점들과 연결되어 있는 지 확인하기 위하여 2차원 리스트 생성
graph = [[] for i in range(N+1)]

for _ in range(M):
    u, v = map(int, input().split())
    # 점들은 서로 연결되어 있음을 표현
    graph[u].append(v)
    graph[v].append(u)

cnt = 0
# 모든 점들은 탐색 전이므로 False로 초기화
visited = [False] * (N+1)

for line in range(1, N+1):
    # 거치지 않은 점이라면 간선이 1개 더 증가하기 때문에 if문 사용
    if visited[line] == False:
        bfs(line)
        # bfs가 끝날 시기에는 간선 한개를 탐색 완료했기 때문에 cnt 증가
        cnt += 1
print(cnt)