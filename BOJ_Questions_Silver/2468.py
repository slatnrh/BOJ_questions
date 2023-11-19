from collections import deque
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 8)

# 상하좌우 설정
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

# dfs
def dfs(x, y, num):
    # (x, y)의 상하좌우 찾기
    for l in range(4):
        nx = x + dx[l]
        ny = y + dy[l]

        # 찾는 영역 주변에 만족하는 영역이 있다면 visited
        if (N > nx >= 0) and (N > ny >= 0) and visited[nx][ny] == 0:
            if area[nx][ny] > num:
                visited[nx][ny] = 1
                dfs(nx, ny, num)

N = int(input())
area = []
maxNum = 0
max_lst = []

for i in range(N):
    area.append(list(map(int, input().split())))
    for j in range(N):
        # 1 ~ maxNum까지 탐색할 것이기 때문에 maxNum 찾기
        if area[i][j] > maxNum:
            maxNum = area[i][j]

for i in range(maxNum):
    visited = [[0]*N for _ in range(N)]
    cnt = 0

    for j in range(N):
        for k in range(N):
            # 조건 만족하면서 not visited 탐색
            if area[j][k] > i and visited[j][k] == 0:
                cnt += 1
                visited[j][k] = 1
                dfs(j, k, i)
    max_lst.append(cnt)

print(max(max_lst))