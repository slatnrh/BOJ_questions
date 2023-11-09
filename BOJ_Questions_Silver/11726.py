import sys
input = sys.stdin.readline

n = int(input())

# dp[0] = 0으로 설정한 이유는 dp[i] = dp[i-1] + dp[i-2]로 가시화하기 좋게 하기 위함
dp = [0, 1, 2]

# 1, 2는 직접 설정 후 3부터 memoization
for i in range(3, n+1):
    dp.append(dp[i-1] + dp[i-2])
print(dp[n] % 10007)