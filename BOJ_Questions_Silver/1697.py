from collections import deque

def bfs():
    # LIFO FIFO 둘다 이용할 것이라 deque 사용
    q = deque()
    # 0번째 위치 저장
    q.append(N)

    while q:
        # 저장된 위치에서 +1, -1, *2를 한 값을 저장, location array에 순서 저장
        x = q.popleft()
        # 저장한 위치과 도착 지점이 같을 경우
        if x == K:
            # 그 위치의 순서 출력
            print(location[x])
            break
        # -1, +1, *2 저장, 순서 +1
        for nx in (x - 1, x + 1, x * 2):
            if 0 <= nx <= MAX and not location[nx]:
                location[nx] = location[x] + 1
                q.append(nx)

# 시간초과 방지용 (100000까지 입력 받을 수 있음)
MAX = 10**5
location = [0] * (MAX + 1)
N, K = map(int, input().split())

bfs()