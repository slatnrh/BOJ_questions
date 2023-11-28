import sys
input = sys.stdin.readline

# 카잉 달력 구현
def calendar(M, N, x, y):
    while x <= M * N:
        # y에 N을 계속 더해줌(x+M*a == y+N*b가 성립해야됨)
        if (x - y) % N == 0:
            return x
        # x에 M을 계속 더해줌
        x += M
    return -1

T = int(input())

for _ in range(T):
    M, N, x, y = map(int, input().split())
    print(calendar(M, N, x, y))