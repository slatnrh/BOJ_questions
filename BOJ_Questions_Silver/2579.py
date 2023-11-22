import sys
input = sys.stdin.readline

stairs = int(input())

# 300칸 이하이기 때문에 [0] * 301로 초기화(백준 문제에서 런타임에러 발생)
stairs_lst = [0] * 301
for i in range(1, stairs + 1):
    stairs_lst[i] = int(input())

dp = [0] * 301
# dp[1], dp[2], dp[3]을 초기화 해야 점화식 적용 가능
dp[1] = stairs_lst[1]
dp[2] = stairs_lst[1] + stairs_lst[2]
# 1층 or 2층 중 숫자가 더 큰 계단을 밟고 3층을 밟아야 됨
dp[3] = max(stairs_lst[1] + stairs_lst[3], stairs_lst[2] + stairs_lst[3])

for i in range(4, stairs + 1):
    # 1칸 낮은 계단과 2칸 낮은 계단을 밟고 올라왔을 때 어디가 더 큰 값을 가지는 지 비교
    dp[i] = max(dp[i-3] + stairs_lst[i-1] + stairs_lst[i], dp[i-2] + stairs_lst[i])

print(dp[stairs])