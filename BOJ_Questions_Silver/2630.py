import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 8)

N = int(input())

paper = [list(map(int, input().split())) for _ in range(N)] 

# 0으로 된 색종이와 1로 된 색종이의 수 저장 list
result = []
# 분할 정복
# (0, 0)에서 시작하여 자신이 설정한 색종이가 모두 같은 값을 가지면 그 값 저장
# 그렇지 않다면 4등분하여 재탐색
def divide_and_conquer(x, y, N):
  color = paper[x][y]
  # 모든 항 같은 값인지 확인
  for i in range(x, x+N):
    for j in range(y, y+N):
        # 같지 않은 값 발견 시
        if color != paper[i][j]:
            # 4등분하여 재탐색
            divide_and_conquer(x, y, N//2)
            divide_and_conquer(x, y+N//2, N//2)
            divide_and_conquer(x+N//2, y, N//2)
            divide_and_conquer(x+N//2, y+N//2, N//2)
            # return을 안해준다면 if문 종료 후 4등분 하기 전 함수로 재귀하여 재탐색함. 0과 1을 쓸데없이 더 저장하게 되는 상황 발생
            return
  if color == 0:
    result.append(0)
  else:
    result.append(1)

# (0, 0)에서 시작
divide_and_conquer(0,0,N)
print(result.count(0))
print(result.count(1))