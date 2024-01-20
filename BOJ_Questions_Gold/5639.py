import sys
sys.setrecursionlimit(10 ** 8)
input = sys.stdin.readline

tree_lst = []
while True:
    try:
        tree_lst.append(int(input()))
    # 입력을 다 받고 난 후
    except:
        break

def post(start, end):
    # 더 작은 노드가 없을 시
    if start > end:
        return

    mid = end + 1
    for i in range(start + 1, end + 1):
        # 트리의 왼쪽, 오른쪽 구분 분기점
        if tree_lst[i] > tree_lst[start]:
            mid = i
            break
    
    post(start + 1, mid - 1) # 왼쪽 트리
    post(mid, end) # 오른쪽 트리
    print(tree_lst[start]) # 루트 노드 출력(왼쪽 루트 마지막 노드)

post(0, len(tree_lst) - 1) # 첫 전체 트리