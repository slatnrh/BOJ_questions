from collections import deque
import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    queue = deque(list(map(int, sys.stdin.readline().split())))
    count = 0
    while queue:
        best = max(queue)
        front = queue.popleft()
        M -= 1

        if best == front:
            count += 1
            if M < 0:
                print(count)
                break

        else:
            queue.append(front)
            if M < 0 :
                M = len(queue) - 1