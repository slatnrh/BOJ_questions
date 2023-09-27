import sys
input = sys.stdin.readline

N = int(input())

lst = []
for _ in range(N):
    command = input().split()

    if command[0] == 'push':
        lst.append(command[1])
        continue
    if command[0] == 'pop':
        if len(lst) == 0:
            print('-1')
            continue
        else:
            print(lst.pop(0))
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