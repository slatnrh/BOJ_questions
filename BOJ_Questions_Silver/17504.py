import sys
input = sys.stdin.readline

# GCD_AND_LCM: 최대공약수 찾기
def GCD_AND_LCM(numerator, denominator):
    gcd, lcm = 0
    i = 1
    while (1 <= numerator and i <= denominator):
        if (numerator % i == 0 and denominator % i == 0):
            gcd = i
    lcm = (numerator * denominator) // gcd
    return gcd, lcm


N = int(input())

a = list(map(int, input().split()))

# 분수 기본 설정
numerator = 1
denominator = a[N-1]

for i in range(N-1):
    # a[-2]부터 시작 -> 분자 = 분자 + a[-2] * 분모
    numerator = numerator + a[(N-2)-i]*denominator
    # 분자 분모 뒤집기
    numerator, denominator = denominator, numerator

# 1 - 분수를 표현
numerator = denominator - numerator

# 만약 기약분수가 아니라면 최대공약수로 나눠서 기약분수 표현
if denominator % numerator == 0:
    numerator, denominator = GCD_AND_LCM(numerator, denominator)

print(numerator, denominator)