X = int(input())

cnt = 0
rslt = 0
temp = 1
while True:
    if temp == X:
        cnt += 1
        break
    elif temp < X:
        temp = temp << 1
    else:
        rslt += temp >> 1
        X -= temp >> 1
        temp = 1
        cnt += 1
print(cnt)