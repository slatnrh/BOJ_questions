# min_cost: dynamic programming을 활용하여 이전 집까지의 최솟값 + 현재 집 찾기
def min_cost(N, RGB_cost):
    dp = [[0] * 3 for _ in range(N)]
    # 첫 번째 집의 비용은 초기값으로 설정
    dp[0] = RGB_cost[0]
    
    # 점화식을 이용하여 dp 테이블 채우기
    for i in range(1, N):
        dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + RGB_cost[i][0]
        dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + RGB_cost[i][1]
        dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + RGB_cost[i][2]
    
    # 마지막 집에서의 최소 비용 반환
    return min(dp[N-1])

N = int(input())
RGB_cost = [list(map(int, input().split())) for _ in range(N)]

result = min_cost(N, RGB_cost)
print(result)