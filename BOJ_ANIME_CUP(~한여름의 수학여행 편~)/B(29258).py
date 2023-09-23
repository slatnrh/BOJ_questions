T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    i = 0

    while True:
        if N % 2 == 0 and 2 * M >= N:
            i += N // 2
            print(i)
            break
        if N % 2 == 0 and 2 * M < N:
            i += M
            if N - M < 0:
                break
            N -= M
        if N % 2 == 1 and N < 3 * M:
            i += M + (N - M) // 2
            print(i)
            break
        if N % 2 == 1 and N >= 3 * M:
            N -= M
            i += M