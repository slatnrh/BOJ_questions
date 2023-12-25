from collections import deque
import sys
input = sys.stdin.readline

def bfs(x, y):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    queue = deque()
    queue.append((x, y))

    # 첫번째 가구: count 수 증가 및 방문 기록 저장
    count = 1
    visited[x][y] = True

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 방문 기록 저장 & 주위 가구 존재 유무 파악 & count 수 증가
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and map[nx][ny] == '1':
                visited[nx][ny] = True
                queue.append((nx, ny))
                count += 1
    
    return count

N = int(input())

map = []
for _ in range(N):
    map.append(list(input().strip()))

visited = [[False] * N for _ in range(N)]

result = []
# 지도 상에 1을 찾고 방문하지 않았다면 bfs 시작
for i in range(N):
    for j in range(N):
        if map[i][j] == '1' and not visited[i][j]:
            # bfs 결과값(붙어있는 총 가구 수)를 result 리스트에 append
            result.append(bfs(i, j))

# 오름차순으로 출력해야하기 때문에 정렬
result.sort()

# 붙어있는 가구들의 수 & 각 가구들의 수 출력
print(len(result))
for estate in result:
    print(estate)