import sys
input = sys.stdin.readline

N, M = map(int, input().split())
# [1:]을 한 이유: 몇 명을 받을지 적은 [0]은 중요하지 않아서 버림
know_truth = set(input().split()[1:])
parties = []

for _ in range(M):
    # line 5와 같은 이유로 중요하지 않아서 버림
    # parties 리스트에 party의 참가자를 append
    parties.append(set(input().split()[1:]))

for _ in range(M):
    for party in parties:
        # 파티에 참여한 사람 중 진실을 아는 사람이 1명이라도 있을 경우
        # &: and 연산자 -> party와 know_truth에 같은 값이 있을 경우 그 값 추가
        if party & know_truth:
            # 모두가 진실을 알게 되므로 knowList에 명단 추가
            # .union: 합집합
            know_truth = know_truth.union(party)

cnt = 0
# 정보) knowList에는 현재 최종적으로 진실을 알게 되는 사람들이 다 모여있음
for party in parties:
    # party에 참가한 인원 중 진실을 아는 사람이 1명이라도 있을 경우
    if party & know_truth:
        # 다음 파티로 넘어감
        continue
    # 없다면 그 파티에서는 거짓말을 할 수 있으므로 cnt += 1
    cnt += 1

print(cnt)