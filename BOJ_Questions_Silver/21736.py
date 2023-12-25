from collections import deque
import sys
input = sys.stdin.readline

def bfs(start):
    global cnt
    direction = [(1,0), (0,1), (-1,0), (0,-1)]
    visited = [[False] * M for _ in range(N)]

    queue = deque([start])
    visited[start[0]][start[1]] = True
    while(queue):
        x, y = queue.popleft()
        
        for dx, dy in direction:
            nx, ny = x + dx, y + dy
            
            # 캠퍼스를 벗어나지 않는 구역이고
            if 0 <= nx < N and 0 <= ny < M:
                # 벽이 아니고 방문하지 않은 곳이면 방문
                if campus[nx][ny] != 'X' and not visited[nx][ny]:
                    queue.append((nx, ny))
                    visited[nx][ny] = True
                    
                    # 사람이면 +1
                    if campus[nx][ny] == 'P':
                        cnt += 1
                    

N, M = map(int, input().split())

campus = []
start = ()
cnt = 0

for i in range(N):
    row = list(input().rstrip())
    for j in range(M):  # 시작점 찾기
        if row[j] == 'I':
            start = (i, j)
    campus.append(row)

bfs(start)
    
print(cnt if cnt > 0 else 'TT')