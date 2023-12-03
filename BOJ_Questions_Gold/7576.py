import sys
input = sys.stdin.readline
from collections import deque

# bfs: 토마토 익는 날짜를 queue에 저장
def bfs():
    # 상하좌우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and tomato_box[nx][ny] == 0:
                # 이전 날짜 +1
                tomato_box[nx][ny] = tomato_box[x][y] + 1
                queue.append([nx, ny])

M, N = map(int, input().split())
tomato_box = [list(map(int, input().split())) for _ in range(N)]
queue = deque([])
cnt = 0

for i in range(N):
    for j in range(M):
        if tomato_box[i][j] == 1:
            queue.append([i, j])

bfs()
for i in tomato_box:
    for j in i:
        # 0이 남는 다는 것은 토마토가 절대 익지 않는다는 뜻
        if j == 0:
            # -1 출력 후 프로그램 종료
            print(-1)
            exit(0)
    cnt = max(cnt, max(i))
# 처음 날짜를 1로 지정했기 때문에 -1
print(cnt - 1)