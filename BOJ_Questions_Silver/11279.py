# 파이썬 heapq 모듈은 heapq (priority queue) 알고리즘을 제공함
import heapq
import sys
input = sys.stdin.readline

N = int(input())
heap = []
for _ in range(N):
    x = int(input())

    # 0을 입력받았을 때 heap에 최댓값 출력
    # 0이 아닌 자연수를 입력받았을 때 heap에 저장, 최솟값을 출력하기 위해 -value로 저장
    if x != 0:
        heapq.heappush(heap, -x)
    else:
        # 기본적으로 heappop은 최솟값을 출력하기에 -value로 저장 후 출력을 -(-value)로 해야됨
        if heap:
            print(-heapq.heappop(heap))
        # heap이 비어있을 때 0 출력
        else:
            print('0')