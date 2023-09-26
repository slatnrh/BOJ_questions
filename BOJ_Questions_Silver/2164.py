from collections import deque

N = int(input())
deque_arr = deque([i for i in range(1, N+1)])

while len(deque_arr) > 1:
    deque_arr.popleft()
    num = deque_arr.popleft()
    deque_arr.append(num)

print(deque_arr[0])