import heapq, sys
input = sys.stdin.readline

dual_priority_queue_min = []    # 최소 힙
dual_priority_queue_max = []    # 최대 힙
removed = set()

T = int(input())

for i in range(T):
    # 새 배열을 받아야 해서 clear
    dual_priority_queue_min.clear()
    dual_priority_queue_max.clear()
    removed.clear()

    k = int(input())

    for order in range(k):
        command, n = input().split()
        n = int(n)

        if command == 'I':  # I: 배열에 입력
            heapq.heappush(dual_priority_queue_max, (-n, order))
            heapq.heappush(dual_priority_queue_min, (n, order))
        elif command == 'D':    # D: 1일 경우 최대값, -1일 경우 최솟값 pop
            if n == 1:
                # max heap에 value가 존재 & removed에 저장된 순서가 있으면
                while dual_priority_queue_max and dual_priority_queue_max[0][1] in removed:
                    # min heap or max heap 둘 중 하나에 없기 때문에 pop
                    heapq.heappop(dual_priority_queue_max)
                # max heap에 value가 존재하면
                if dual_priority_queue_max:
                    # removed에 순서 저장(min heap, max heap 둘 다 소거하기 위해)
                    removed.add(dual_priority_queue_max[0][1])
                    heapq.heappop(dual_priority_queue_max)
            elif n == -1:
                # min heap에 value가 존재 & removed에 저장된 순서가 있으면
                while dual_priority_queue_min and dual_priority_queue_min[0][1] in removed:
                    # min heap or max heap 둘 중 하나에 없기 때문에 pop
                    heapq.heappop(dual_priority_queue_min)
                # min heap에 value가 존재하면
                if dual_priority_queue_min:
                    # removed에 순서 저장(min heap, max heap 둘 다 소거하기 위해)
                    removed.add(dual_priority_queue_min[0][1])
                    heapq.heappop(dual_priority_queue_min)

    # max heap에 value가 존재하고 removed set에 max heap[0][1]이 존재하면 pop
    while dual_priority_queue_max and dual_priority_queue_max[0][1] in removed:
        heapq.heappop(dual_priority_queue_max)
    # min heap에 value가 존재하고 removed set에 min heap[0][1]이 존재하면 pop
    while dual_priority_queue_min and dual_priority_queue_min[0][1] in removed:
        heapq.heappop(dual_priority_queue_min)

    if not dual_priority_queue_max or not dual_priority_queue_min:
        print("EMPTY")
    else:
        # max값은 음수로 저장되어 있어 -(-)로 출력해야 하기 때문에 -가 붙어 나옴
        print(-dual_priority_queue_max[0][0], dual_priority_queue_min[0][0])