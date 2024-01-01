from collections import deque
import sys
input = sys.stdin.readline

# bfs: 치즈 주변 공기 접촉 부위 True로 바꾸기
def bfs(cheese, air, N, M):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    queue = deque()
    queue.append((0, 0))
    air[0][0] = True

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < M and not air[nx][ny]:
                if cheese[nx][ny] == 0:
                    air[nx][ny] = True
                    queue.append((nx, ny))

# melt_cheese: 접촉 부위가 2개 이상인 치즈 찾아서 녹이기(0으로 바꾸기)
def melt_cheese(cheese, air, N, M):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    melted = []

    for x in range(N):
        for y in range(M):
            if cheese[x][y] == 1:
                cnt = 0
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]

                    if 0 <= nx < N and 0 <= ny < M and air[nx][ny]:
                        cnt += 1
                if cnt >= 2:
                    melted.append((x, y))

    for x, y in melted:
        cheese[x][y] = 0

    return melted

# bfs, melted_cheese 함수를 치즈가 없을 때까지 돌리기 -> 있을때마다 days += 1, 없으면 days return
def count_days(cheese, N, M):
    days = 0
    while True:
        air = [[False] * M for _ in range(N)]
        bfs(cheese, air, N, M)
        melted_cheese = melt_cheese(cheese, air, N, M)

        if not melted_cheese:
            break
        days += 1

    return days


N, M = map(int, input().split())
cheese_board = []
for _ in range(N):
    cheese_board.append(list(map(int, input().split())))

result = count_days(cheese_board, N, M)
print(result)
