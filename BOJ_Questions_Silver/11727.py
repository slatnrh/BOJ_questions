import sys
input = sys.stdin.readline

n = int(input())
# dp[2] == 3을 만족시키기 위해 dp[0]을 1로 설정
dp = [1, 1]

for i in range(2, n+1):
    # 2*1 타일은 dp[n-1], 1*2와 2*2는 dp[n-2]에서 추가 되는 것이기 때문에 위와 같은 식이 성립
    dp.append(dp[i-1] + 2*dp[i-2])

print(dp[n] % 10007)