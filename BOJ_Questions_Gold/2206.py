from collections import deque
import sys
input = sys.stdin.readline

def bfs():
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    queue = deque()
    queue.append((0, 0, 1, 0))

    while queue:
        x, y, count, smashed = queue.popleft()

        # 종점 도착
        if x == N - 1 and y == M - 1:
            return count

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < M:
                if graph[nx][ny] == 0 and not visited[nx][ny][smashed]:
                    visited[nx][ny][smashed] = True
                    queue.append((nx, ny, count + 1, smashed))
                # 칸이 1이고 부순 적 없을 때
                elif graph[nx][ny] == 1 and not smashed and not visited[nx][ny][1]:
                    visited[nx][ny][1] == True
                    # 마지막 인자를 1로 놓음으로써 부순 흔적 남기기
                    queue.append((nx, ny, count + 1, 1))
    # 종점 도착 못할 시 -1 return
    return -1


N, M = map(int, input().split())

graph = []
for _ in range(N):
    graph.append(list(map(int, input().rstrip())))

# 벽 부순 여부 확인 위해 3차원 배열
visited = [[[False] * 2 for i in range(M)] for j in range(N)]

result = bfs()
print(result)