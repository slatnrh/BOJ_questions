import sys
input = sys.stdin.readline

N, M = map(int, input().split())

dic = dict()
for i in range(1, N+1):
    Pokemon = input().strip()
    dic[i] = Pokemon
    dic[Pokemon] = i


for _ in range(M):
    find = input().strip()
    if find.isdigit():
        print(dic[int(find)])
    else:
        print(dic[find])