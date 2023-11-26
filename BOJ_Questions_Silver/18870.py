import sys
input = sys.stdin.readline

N = int(input())
# 초기 좌표 리스트
coordinate = list(map(int, input().split()))
# 중복 제외 초기 리스트 정렬
answer_lst = sorted(list(set(coordinate)))

# 정렬한 리스트 좌표값 dict로 0부터 순서 매기기
dic = {answer_lst[i] : i for i in range(len(answer_lst))}
# 초기 좌표들의 순서 출력
for i in coordinate:
    print(dic[i], end = ' ')