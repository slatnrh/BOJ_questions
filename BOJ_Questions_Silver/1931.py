import sys
input = sys.stdin.readline

N = int(input())
# 회의 시작 시각과 끝나는 시각을 튜플로 묶어서 리스트 append
time = [tuple(map(int, input().split())) for _ in range(N)]

# 끝나는 시간을 기준으로 정렬
time = sorted(time, key = lambda x:(x[1], x[0]))

meeting_num = end_time = 0
for start, end in time:
    # 시작 시각이 마지막 회의의 끝나는 시각보다 클때
    if start >= end_time:
        # 끝나는 시각 초기화, 회의수 += 1
        end_time = end
        meeting_num += 1
print(meeting_num)