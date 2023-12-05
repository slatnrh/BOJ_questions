# 이분 탐색 써야 시간 초과 안 걸림
def binary_search(tree_lst, M, start, end):
    while start <= end:
        mid = (start + end) // 2

        tree = 0
        for i in tree_lst:
            # 자른 나무보다 크면
            if i >= mid:
                # 남은 나무 길이 +
                tree += i - mid
        if tree >= M:
            start = mid + 1
        else:
            end = mid - 1
    print(end)


N, M = map(int, input().split())

tree_lst = list(map(int, input().split()))
start, end = 1, max(tree_lst)

binary_search(tree_lst, M, start, end)