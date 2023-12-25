from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
# 위치 당 방문 순서
game_board = [0] * 101
# 방문 여부: True일 경우 기존 값이 최솟값이기에 넘어가기 위함
visited = [False] * 101

ladder = dict()
snake = dict()

# 사다리를 dictionary 형식으로 저장
for _ in range(N):
    x, y = map(int, input().split())
    ladder[x] = y
# 뱀을 dictionary 형식으로 저장
for _ in range(M):
    u, v = map(int, input().split())
    snake[u] = v

queue = deque([1])

while queue:
    position = queue.popleft()
    # 100에 도달 시 방문 순서 출력
    if position == 100:
        print(game_board[position])
        break
    
    # 1 ~ 6 까지 주사위 다 던져보기
    for dice in range(1, 7):
        next_place = position + dice

        if next_place <= 100 and not visited[next_place]:
            # 사다리가 있을 때 다음 위치는 사다리 탄 후 위치
            if next_place in ladder.keys():
                next_place = ladder[next_place]
            # 뱀이 있을 때 다음 위치는 뱀 탄 후 위치
            if next_place in snake.keys():
                next_place = snake[next_place]
            # 아무것도 없을 때 순서 +1
            if not visited[next_place]:
                visited[next_place] = True
                game_board[next_place] = game_board[position] + 1
                queue.append(next_place)