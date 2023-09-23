import sys

N = int(sys.stdin.readline())

lst = []

for i in range(N):
    lst.append(sys.stdin.readline().strip())

rslt = set(lst)
rslt = list(rslt)
rslt.sort()
rslt.sort(key = len)


for i in rslt:
    print(i)