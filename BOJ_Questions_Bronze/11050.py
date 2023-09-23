def Factorial(n):
    if n == 0:
        return 1
    return n * Factorial(n-1)

import sys

N, K = map(int, sys.stdin.readline().split())

mother = Factorial(N)
son = Factorial(K) * Factorial(N-K)

print(mother // son)