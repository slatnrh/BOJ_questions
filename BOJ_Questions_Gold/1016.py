# remain 변수: min_num보다 작은 값은 출력할 필요 X(출처: https://imksh.com/69)
# remain 값에 따라 보정 가능(0일때에는 제곱수로 나눠진다는 뜻이므로 그대로 사용, 1일때는 +1을 해줌으로써 min_num보다 큰 가장 작은 2의 배수 사용)
import sys
input = sys.stdin.readline

def solution(min_num, max_num):
    answer = max_num - min_num + 1
    check = [False] * (max_num - min_num + 1)
    i = 2
    while i ** 2 <= max_num:
        # 제곱수
        square_num = i ** 2
        # remain 변수는 제곱수가 아닐때 보정시켜서 다음 2의 배수부터 접근하게 한다
        remain = 0 if min_num % square_num == 0 else 1
        j = min_num // square_num + remain

        # 제곱수의 j배 (에라토스테네스의 체)
        while square_num * j <= max_num:
            if not check[square_num * j - min_num]:
                check[square_num * j - min_num] = True
                answer -= 1
            j += 1
        i += 1
    return answer

a, b = map(int,input().split())
rslt = solution(a, b)
print(rslt)