# 풀기 너무 어려워서 챗gpt 활용함 나중에 코드 보고 다시 풀어보기

def visit_order(N, r, c):
    # N = 0일 때 좌표가 생성되지 않음 == 0
    if N == 0:
        return 0
    
    # 1 ~ 4사분면으로 나눠서
    half = 2 ** (N - 1)
    # 어디에 해당되는 지 찾기
    quadrant = 1 if r < half and c < half else 2 if r < half else 3 if c < half else 4
    
    if quadrant == 1:
        # 1사분면: N이 하나 줄고 거기에서 r행 c열을 찾기
        return visit_order(N - 1, r, c)
    elif quadrant == 2:
        # 숫자가 half ** 2를 더한 상태에서 찾아야함, 2사분면이기 때문에 c - half 해주기 
        return half ** 2 + visit_order(N - 1, r, c - half)
    elif quadrant == 3:
        return 2 * (half ** 2) + visit_order(N - 1, r - half, c)
    elif quadrant == 4:
        return 3 * (half ** 2) + visit_order(N - 1, r - half, c - half)

N, r, c = map(int, input().split())
result = visit_order(N, r, c)
print(result)