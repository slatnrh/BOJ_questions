import sys

N = int(sys.stdin.readline())
A = set(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))

print(A)
print(lst)

for i in lst:
    if i in A:
        print(1)
    else:
        print(0)