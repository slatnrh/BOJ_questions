import sys
N, M, B = map(int,input().split())
land = []
for _ in range(N):
    land.append([int(x) for x in sys.stdin.readline().rstrip().split()])

# 최대치: 1e9 == 1*10^9
time = int(1e9)
block = 0

for i in range(257): #땅 높이
    use_block = 0
    take_block = 0
    for x in range(N):
        for y in range(M):
            # 설정한 땅의 높이가 land[x][y]보다 작을때
            if land[x][y] > i:
                # land[x][y] 땅의 높이를 낮춰야 함
                take_block += land[x][y] - i
            # 설정한 땅의 높이가 land[x][y]보다 클때
            else:
                # land[x][y] 땅의 높이를 높여야 함
                use_block += i - land[x][y]
    # 사용한 블럭이 얻은 블럭 + 인벤토리에 있던 블럭보다 크면 배열에 넣지 않기
    if use_block > take_block + B:
        continue
    # 블럭을 캐는건 2초, 쌓는 건 1초 걸림
    count = take_block * 2 + use_block

    if count <= time:
        time = count
        block = i

print(time, block)