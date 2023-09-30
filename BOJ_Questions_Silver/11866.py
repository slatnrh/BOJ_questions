import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())

deq = deque([i for i in range(1, N+1)])

lst = []
while len(deq) != 0:
    for _ in range(K-1):
        deq.append(deq.popleft())
    lst.append(str(deq.popleft()))

print('<'+', '.join(lst)+'>')