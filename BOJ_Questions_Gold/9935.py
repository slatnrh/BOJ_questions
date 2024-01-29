import sys
input = sys.stdin.readline

line = input().strip()
boom = input().strip()

stack = []
boom_len = len(boom)

for i in range(len(line)):
    stack.append(line[i])
    # boom 길이만큼 stack 끝에서 확인 후 boom과 값이 동일한 경우
    if ''.join(stack[-boom_len:]) == boom:
        # boom을 뽑아야 하니 boom의 길이만큼 pop하면 됨
        for _ in range(boom_len):
            stack.pop()

if stack:
    print(''.join(stack))
else:
    print("FRULA")