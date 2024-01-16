# 각 자리 수의 합이 3으로 나누어지면 3의 배수이다
# 30의 배수를 찾아야하니 맨 마지막 자리가 0이어야한다.

n = input()
n = sorted(n, reverse = True)
sum = 0
if '0' not in n:
    print(-1)
else:
    for i in n:
        sum += int(i)
    if sum % 3 != 0:
        print(-1)
    else:
        print(''.join(n))