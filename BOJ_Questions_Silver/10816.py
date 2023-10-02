import sys
input = sys.stdin.readline

def BSearch(lst, target, start, end):
    if start > end:
        return 0
    mid = (start + end) // 2
    if target == lst[mid]:
        return cnt.get(target)
    elif target > lst[mid]:
        return BSearch(lst, target, mid+1, end)
    else:
        return BSearch(lst, target, start, mid-1)


N = int(input())
num_lst = sorted(list(map(int, input().split())))

M = int(input())
cnt_lst = list(map(int, input().split()))

cnt = {}
for i in num_lst:
    if i in cnt:
        cnt[i] += 1
    else:
        cnt[i] = 1

for i in cnt_lst:
    print(BSearch(num_lst, i, 0, len(num_lst)-1), end = ' ')
