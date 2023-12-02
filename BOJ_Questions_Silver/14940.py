import sys
input = sys.stdin.readline
from collections import deque

# bfs: 기존 좌푯값이 2 -> 1, 0 -> 0, 1 -> 이전 좌표값의 +1
def bfs(i,j):
    # 좌표 설정
    dx = [0,0,-1,1]
    dy = [-1,1,0,0]

    coordinate = deque()
    coordinate.append((i,j))
    
    # 2가 적혀있는 곳의 좌표는 0으로 시작
    visited[i][j] = 0

    while coordinate:
        x, y = coordinate.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == -1:
                # 기존 좌푯값이 0이면 visited 값 0
                if map_lst[nx][ny] == 0: 
                    visited[nx][ny] = 0
                # 기존 좌푯값이 1이면 이전 좌푯값 +1
                elif map_lst[nx][ny] == 1:
                    visited[nx][ny] = visited[x][y] + 1
                    # 남은 좌표들 탐색하기 위해 visited에 저장
                    coordinate.append((nx,ny))

N, M = map(int, input().split())
map_lst = [list(map(int, input().split())) for _ in range(N)]

# 0으로 둘러쌓여 있는 좌표는 -1로 출력해야 하기 때문에 -1로 초기화
visited = [[-1] * M for _ in range(N)]

for i in range(N):
    for j in range(M):
        # 지도 좌푯값 2 발견하면 bfs, visited값 -1인지 확인 안하면 컴파일 에러 발생
        if map_lst[i][j] == 2 and visited[i][j] == -1:
            bfs(i,j)

# visited 값 출력
for i in range(N):
    for j in range(M):
        if map_lst[i][j] == 0:
            print(0, end=' ')
        else:
            print(visited[i][j], end=' ')
    print()