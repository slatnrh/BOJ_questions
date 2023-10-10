N = int(input())

j = 0
for i in range(N):
    print(' '*int(i), end = '')
    print('*'*int(N-j))
    j += 1