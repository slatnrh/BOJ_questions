# math 모듈에 있는 math.gcd 함수를 사용하면 쉽게 최소공배수를 구할 수 있다
# def GCD_AND_LCM(numerator, denominator):
#     gcd = math.gcd(numerator, denominator)
#     lcm = (numerator * denominator) // gcd
#     return gcd, lcm

def GCD_AND_LCM(numerator, denominator):
    i = 1
    gcd = 1
    while i <= numerator and i <= denominator:
        if numerator % i == 0 and denominator % i == 0:
            gcd = i
        i += 1
    lcm = (numerator * denominator) // gcd
    return gcd, lcm

T = int(input())

for _ in range(T):
    A, B = map(int, input().split())
    result_gcd, result_lcm = GCD_AND_LCM(A, B)
    print(result_lcm)