import sys
input = sys.stdin.readline

# 0번째 숫자 없애기
timenum_lst = [0]

i = j = k = l = 1
while True:
    # 배열에 시계수 넣기
    timenum = min(1000*i + 100*j + 10*k + l, 1000*j + 100*k + 10*l + i, 1000*k + 100*l + 10*i + j, 1000*l + 100*i + 10*j + k)
    # 이전에 만든 시계수가 있다면 넣지 않기
    if timenum not in timenum_lst:
        timenum_lst.append(timenum)
    
    # 숫자를 하나씩 늘려가면서 브루트포스
    l += 1
    if l >= 10:
        k += 1
        l = 1
    if k >= 10:
        j += 1
        k = 1
    if j >= 10:
        i += 1
        j = 1
    if i >= 10:
        break
# 시계수 값에 따라 정렬하기
timenum_lst.sort()

a, b, c, d = map(int, input().split())
num = min(1000*a + 100*b + 10*c + d, 1000*b + 100*c + 10*d + a, 1000*c + 100*d + 10*a + b, 1000*d + 100*a + 10*b + c)

print(timenum_lst.index(num))