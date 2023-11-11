import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    M, N, K = map(int, input().split())
    field = [[0 for i in range(N)] for j in range(M)]
    