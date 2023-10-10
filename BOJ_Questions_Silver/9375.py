import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    test = int(input())
    dic = dict()
    cnt = dict()
    for i in range(test):
        name, wear = input().split()
        dic[name] = wear
        if wear in cnt:
            cnt[wear] += 1
        else:
            cnt[wear] = 1
    len = 1
    for costume in cnt:
        len *= (cnt[costume]+1)
    print(len-1)
