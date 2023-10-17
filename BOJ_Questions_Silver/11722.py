import sys
input = sys.stdin.readline

A = int(input())
arr = list((map(int, input().split())))

dp = dict()
dp[0] = 1
for i in range(1, A):
    check = []
    for j in range(i):
        if arr[i] < arr[j]:
            check.append(int(dp[j])+1)
    if check != []:
        dp[i] = max(check)
    else:
        dp[i] = 1

print(max(dp.values()))