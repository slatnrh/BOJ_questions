import sys
input = sys.stdin.readline

target = int(input())
n = int(input())
broken = list(map(int, input().split()))

# 현재 채널(100)에서 단순 이동한 경우
min_count = abs(100 - target)

for nums in range(1000001):
    nums = str(nums)
    
    for j in range(len(nums)):
        # 숫자 중 고장 난 것이 있다면 break
        if int(nums[j]) in broken:
            break
        # 고장난 숫자가 없고 마지막 자리까지 왔으면 min_count와 비교
        elif j == len(nums) - 1:
            min_count = min(min_count, abs(int(nums) - target) + len(nums))
print(min_count)