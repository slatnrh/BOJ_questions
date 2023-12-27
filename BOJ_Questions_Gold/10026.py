from collections import deque
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

# bfs: 색 정보 받아서 그 색과 같은 지역 모두 방문 표시
def bfs(x, y, color, visited, grid):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and grid[nx][ny] == color:
                visited[nx][ny] = True
                queue.append((nx, ny))
                bfs(nx, ny, color, visited, grid)


N = int(input())
cnt_normal = 0
cnt_red_green = 0

grid = []
for _ in range(N):
    grid.append(list(map(str, input().strip())))

# 적록색약이 아닌 사람이 봤을 때의 영역구분
visited = [[False]*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            visited[i][j] = True
            bfs(i, j, grid[i][j], visited, grid)
            cnt_normal += 1

# 적록색약인 사람 설정(Green -> Red)
for i in range(N):
    for j in range(N):
        if grid[i][j] == 'G':
            grid[i][j] = 'R'

# 적록색약인 사람이 봤을 때의 영역구분
visited = [[False]*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            visited[i][j] = True
            bfs(i, j, grid[i][j], visited, grid)
            cnt_red_green += 1

print(cnt_normal, cnt_red_green)