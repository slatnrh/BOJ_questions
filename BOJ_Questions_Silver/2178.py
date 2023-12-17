from collections import deque

# bfs: 미로에서 1만 따라가서 최단거리 구하기
def bfs(x,y):
    # 좌표 설정
    dx = [0,0,-1,1]
    dy = [-1,1,0,0]

    queue = deque()
    queue.append((x,y))

    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < N and 0 <= ny < M:
                # 0은 거칠 수 없는 곳
                if maze_lst[nx][ny] == 0:
                    continue
                elif maze_lst[nx][ny] == 1:
                    # 1은 이전 값 +1로 변경해주면서 앞으로 나아가기
                    maze_lst[nx][ny] = maze_lst[x][y] + 1
                    queue.append((nx, ny))
            else:
                continue

    # 최종 좌표인 (N-1, M-1)에서의 maze_lst값 return
    return maze_lst[N-1][M-1]


N, M = map(int, input().split())
maze_lst = []

for _ in range(N):
    maze_lst.append(list(map(int, input())))

# 시작 좌표인 (0, 0)에서 bfs함수 시작 
print(bfs(0, 0))