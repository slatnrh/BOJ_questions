import sys
input = sys.stdin.readline

arr = [1, 1, 1, 2, 2, 3, 4, 5, 7, 9]
T = int(input())

for i in range(10, 101):
    arr.append(arr[i-1] + arr[i-5])


for _ in range(T):
    case = int(input())
    print(arr[case-1])
