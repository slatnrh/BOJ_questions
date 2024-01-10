# 지수 법칙: A^(m + n) = A^m * A^n
# 나머지 분배 법칙: (A * B) % C = (A % C) * (B % C) % C

def power(A, B, C):
    # 지수가 0일 때
    if B == 0:
        return 1 % C
    # 지수가 1일 때
    elif B == 1:
        return A % C
    else:
        # 분할정복 적용
        temp = power(A, B // 2, C)
        # 지수가 짝수일 때
        if B % 2 == 0:
            return (temp * temp) % C
        # 지수가 홀수일 때
        else:
            return (temp * temp * A) % C

A, B, C = map(int, input().split())
result = power(A, B, C)
print(result)