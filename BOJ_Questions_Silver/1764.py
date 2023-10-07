import sys
input = sys.stdin.readline

N, M = map(int, input().split())

didnot_listen = set()
didnot_watch = set()

for _ in range(N):
    person = input().strip()
    didnot_listen.add(person)

for _ in range(M):
    person = input().strip()
    didnot_watch.add(person)

rslt = sorted(list(didnot_listen & didnot_watch))
print(len(rslt))
for i in rslt:
    print(i)