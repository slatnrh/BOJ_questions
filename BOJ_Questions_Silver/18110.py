import sys

input = sys.stdin.readline

def num_round(val):
    return int(val) + (1 if val - int(val) >= 0.5 else 0)
 
n = int(input())
if n:
    arr = []
    for _ in range(n):
        arr.append(int(input()))
    arr.sort()
    num = num_round(n * 0.15)
    print(num_round(sum(arr[num:-num] if num else arr) / (n - 2 * num)))
else:
    print(0)