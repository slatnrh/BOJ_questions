import sys
input = sys.stdin.readline

n = int(input())
cnt = 1
flag = 0
stack = []
rslt = []

for i in range(n):
    num = int(input())
    while cnt <= num:
        stack.append(cnt)
        rslt.append('+')
        cnt += 1
    
    if stack[-1] == num:
        stack.pop()
        rslt.append('-')
    else:
        print("NO")
        flag = 1
        break

if flag == 0:
    for i in rslt:
        print(i)