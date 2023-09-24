import sys

N = int(sys.stdin.readline())

lst = []
for _ in range(N):
    command = sys.stdin.readline().split()

    if command[0] == 'push':
        lst.append(command[1])
        continue
    if command[0] == 'pop':
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
    if command[0] == 'top':
        if len(lst) == 0:
            print('-1')
            continue
        else:
            print(lst[-1])
            continue