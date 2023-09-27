import sys
input = sys.stdin.readline

N = int(input())

for _ in range(N):
    stack = []
    str = input()
    for i in str:
        if i == '(':
            stack.append(i)
        elif i == ')':
            if stack:
                stack.pop()
            else:
                print('NO')
                break
        else:
            if not stack:
                print('YES')
            else:
                print('NO')