# 파이썬 heapq 모듈은 heapq (priority queue) 알고리즘을 제공함
import heapq, sys
input = sys.stdin.readline

N = int(input())
plus_heap = []
minus_heap = []
for _ in range(N):
    x = int(input())
    # 0을 입력받았을 때 heap에 최댓값 출력
    # 0이 아닌 자연수를 입력받았을 때 heap에 저장, 최솟값을 출력하기 위해 -value로 저장
    if x != 0:
        if x > 0:
            heapq.heappush(plus_heap, x)
        else:
            heapq.heappush(minus_heap, -x)
    else:
        # 기본적으로 heappop은 최솟값을 출력하기에 -value로 저장 후 출력을 -(-value)로 해야됨
        if plus_heap:
            if minus_heap:
                if plus_heap[0] < minus_heap[0]:
                    print(heapq.heappop(plus_heap))
                else:
                    print(-heapq.heappop(minus_heap))
            else:
                print(heapq.heappop(plus_heap))
        elif minus_heap:
            print(-heapq.heappop(minus_heap))
        else:
            print('0')