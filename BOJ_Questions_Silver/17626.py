# def: dp[i]는 dp[i-제곱수]+1(제곱수<=i)들 중 가장 작은값을 배열에 저장하면서 Bottom-up 방식으로 dp배열을 채운다
def fourSquares(n):
    dp = [float('inf')] * (n + 1)
    dp[0] = 0

    for i in range(1, n + 1):
        j = 1
        while j * j <= i:
            dp[i] = min(dp[i], dp[i - j * j] + 1)
            j += 1

    return dp[n]

n = int(input())
print(fourSquares(n))