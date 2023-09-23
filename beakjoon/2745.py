N, B = input().split()
N = ''.join(reversed(N))
B = int(B)

number = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
result = 0

for i in range(len(N)-1, -1, -1):
    sum = number.index(N[i]) * (B**i)
    result += sum

print(result)