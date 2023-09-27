from collections import deque
import sys

N = int(sys.stdin.readline())

lst = deque([])
for _ in range(N):
    command = sys.stdin.readline().split()

    if command[0] == 'push_front':
        lst.appendleft(command[1])
        continue
    if command[0] == 'push_back':
        lst.append(command[1])
        continue
    if command[0] == 'pop_front':
        if len(lst) == 0:
            print('-1')
            continue
        else:
            print(lst.popleft())
            continue
    if command[0] == 'pop_back':
        if len(lst) == 0:
            print('-1')
            continue
        else:
            print(lst.pop())
            continue
    if command[0] == 'size':
        print(len(lst))
        continue
    if command[0] == 'empty':
        if len(lst) == 0:
            print('1')
            continue
        else:
            print('0')
            continue
    if command[0] == 'front':
        if len(lst) == 0:
            print('-1')
            continue
        else:
            print(lst[0])
            continue
    if command[0] == 'back':
        if len(lst) == 0:
            print('-1')
            continue
        else:
            print(lst[-1])
            continue