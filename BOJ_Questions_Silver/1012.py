import sys
sys.setrecursionlimit(10 ** 8)
input = sys.stdin.readline

# dfs(matrix[x][y] 주변 배추(1) 찾아서 0으로 변환)
def dfs(x, y):
    # 상하좌우 설정
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    # (x, y)의 상하좌우 찾기
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        # 주변 배추(1) 찾으면 0으로 변환
        if (N > nx >= 0) and (M > ny >= 0):
            if matrix[nx][ny] == 1:
                matrix[nx][ny] = -1
                dfs(nx, ny)

T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())
    matrix = [[0]*M for _ in range(N)]
    cnt = 0
    
    # 배추 심기
    for _ in range(K):
        x, y = map(int, input().split())
        matrix[y][x] = 1
    
    # 심은 배추(1) 찾으면 dfs()를 통해 주변 배추(1) 0으로 변환
    for i in range(N):
        for j in range(M):
            if matrix[i][j] == 1:
                dfs(i, j)
                cnt += 1
    print(cnt)