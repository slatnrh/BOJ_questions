# 파이썬 heapq 모듈은 heapq (priority queue) 알고리즘을 제공함
import heapq
import sys
input = sys.stdin.readline

N = int(input())
heap = []
for _ in range(N):
    x = int(input())

    # 0을 입력받았을 때 heap에 최솟값 출력
    if x == 0:
        if heap:
            print(heapq.heappop(heap))
        # heap이 비어있을 때 0 출력
        else:
            print('0')
    # 0이 아닌 자연수를 입력받았을 때 heap에 저장
    else:
        heapq.heappush(heap, x)