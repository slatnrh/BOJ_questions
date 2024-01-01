import sys
input = sys.stdin.readline

# dfs: 말을 저장하면서 끝까지 가기
# 끝까지 갔다면 백트래킹 방식으로 마지막 말 지우고 다른 방향으로 가서 최댓값 구하기
def dfs(x, y, count):
    global ans
    ans = max(ans, count)
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < R and 0 <= ny < C and not board[nx][ny] in Alphabet_lst:
            Alphabet_lst.add(board[nx][ny])
            dfs(nx, ny, count+1)
            Alphabet_lst.remove(board[nx][ny])

R, C = map(int, input().split())

board = []
for _ in range(R):
    board.append(list(input()))

ans = 0
Alphabet_lst = set()
Alphabet_lst.add(board[0][0])
dfs(0, 0, 1)
print(ans)