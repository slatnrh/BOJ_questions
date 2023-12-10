# 파이썬 heapq 모듈은 heapq (priority queue) 알고리즘을 제공함
import heapq, sys
input = sys.stdin.readline

N = int(input())
# 양수끼리 모아놓은 배열
plus_heap = []
# 음수끼리 모아놓은 배열
minus_heap = []
for _ in range(N):
    x = int(input())

    if x != 0:
        if x > 0:
            heapq.heappush(plus_heap, x)
        else:
            # heap은 기본적으로 정렬을 하기 때문에 음수들을 양수로 저장하기 위해 -를 붙여 append
            heapq.heappush(minus_heap, -x)
    else:
        if plus_heap:
            if minus_heap:
                # 절댓값이 양수[0]이 더 작을 경우
                if plus_heap[0] < minus_heap[0]:
                    print(heapq.heappop(plus_heap))
                # 절댓값이 음수[0]이 더 작을 경우
                else:
                    print(-heapq.heappop(minus_heap))
            # 음수가 없을 경우
            else:
                print(heapq.heappop(plus_heap))
        # 양수가 없을 경우
        elif minus_heap:
            print(-heapq.heappop(minus_heap))
        # 아무런 수가 없을 경우
        else:
            print('0')