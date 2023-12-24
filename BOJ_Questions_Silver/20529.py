import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    sum = sys.maxsize
    mbti_lst = list(map(str, input().split()))

    # N이 32가 넘어가면 mbti 중 하나는 적어도 3개 이상을 갖고 있기 때문에 0을 출력함
    if N > 32:
        print(0)
        continue

    for i in range(N):
        for j in range(N):
            for k in range(N):
                rslt = 0
                # i, j, k 중 같은 게 있으면 자신과 자신을 비교하는 셈이기 때문에 continue
                if i == j or j == k  or k == i:
                    continue
                # mbti에서 다른 게 있을 때마다 +1
                for x in range(4):
                    if mbti_lst[i][x] != mbti_lst[j][x]:
                        rslt += 1
                    if mbti_lst[j][x] != mbti_lst[k][x]:
                        rslt += 1
                    if mbti_lst[k][x] != mbti_lst[i][x]:
                        rslt += 1
                # 가장 최솟값을 뽑아야 하기 때문에 항상 최솟값 비교하기
                sum = min(sum, rslt)
    print(sum)