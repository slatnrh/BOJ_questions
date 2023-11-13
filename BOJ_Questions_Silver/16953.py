import sys
input = sys.stdin.readline

A, B = map(int, input().split())

cnt = 1
while True:
    if A > B:
        print("-1")
        break
    elif A == B:
        print(cnt)
        break

    if B % 10 == 1:
        B //= 10
        cnt += 1
    elif B % 2 == 0:
        B //= 2
        cnt += 1
    else:
        print("-1")
        break