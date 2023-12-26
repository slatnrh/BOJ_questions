from collections import deque
import sys
input = sys.stdin.readline

# bfs: 1을 찾은 후 주위 0에 접근하면서 토마토를 1로 변경 & 날짜 +1 하는 방식
# 그 후 모든 토마토 검사하여 안 익은 토마토 존재 시 -1 출력, 다 익으면 days 출력
def bfs(tomatoes, ripe):
    # 상하좌우위아래 이동을 위한 방향 설정
    dx = [-1, 1, 0, 0, 0, 0]
    dy = [0, 0, -1, 1, 0, 0]
    dz = [0, 0, 0, 0, -1, 1]

    # 최소 일수 계산
    while ripe:
        x, y, z, days = ripe.popleft()

        for i in range(6):
            nx, ny, nz = x + dx[i], y + dy[i], z + dz[i]
            if 0 <= nx < M and 0 <= ny < N and 0 <= nz < H and tomatoes[nz][ny][nx] == 0:
                tomatoes[nz][ny][nx] = days + 1
                ripe.append((nx, ny, nz, days + 1))


# 모든 토마토가 익었는지 확인
    for z in range(H):
        for y in range(N):
            for x in range(M):
                # 안 익은 토마토 존재
                if tomatoes[z][y][x] == 0:
                    return -1
    # 안 익은 토마토 존재 X
    return days


M, N, H = map(int, input().split())
tomatoes = []
for _ in range(H):
    layer = []
    for _ in range(N):
        row = list(map(int, input().split()))
        layer.append(row)
    tomatoes.append(layer)

# 익은 토마토 위치 찾기
ripe = deque()
for z in range(H):
    for y in range(N):
        for x in range(M):
            # 익은 토마토 존재 시
            if tomatoes[z][y][x] == 1:
                # x, y, z 위치와 일수 저장
                ripe.append((x, y, z, 0))

result = bfs(tomatoes, ripe)
print(result)