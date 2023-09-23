import sys

N = int(sys.stdin.readline())

pos_lst = []
for i in range(N):
    x, y = map(int, sys.stdin.readline().split())
    pos_lst.append((x, y))

pos_lst.sort()

for i in pos_lst:
    print(i[0], i[1])