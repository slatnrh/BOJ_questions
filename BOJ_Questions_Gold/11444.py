# 행렬의 거듭제곱과 분할정복을 사용하면 풀이가 쉬워짐(출처: https://ataraxiady.github.io/dev/2021/04/15/dev-boj-2_11444/)
# (F_n+2)   (1 1) (F_n+1)
#         = 
# (F_n+1)   (1 0) (F_n)

import sys
input = sys.stdin.readline
p = 1000000007

# 제곱을 구하는 분할정복
def power(matrix, n):
    if n == 1:
        return matrix
    elif n % 2:
        return multi(power(matrix, n - 1), matrix)
    else:
        return power(multi(matrix, matrix), n // 2)

# 행렬의 곱셈
def multi(a, b):
    temp = [[0] * len(b[0]) for _ in range(2)]
    for i in range(2):
        for j in range(len(b[0])):
            sum = 0
            for k in range(2):
                sum += a[i][k] * b[k][j]
            temp[i][j] = sum % p
    return temp

# 초기 행렬
matrix = [[1, 1], [1, 0]]

# 피보나치 초기값
start = [[1], [1]]

n = int(input())
if n < 3:
    print(1)
else:
    print(multi(power(matrix, n - 2), start)[0][0])