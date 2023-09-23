N, B = map(int, input().split())
lst = []
number = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

while N:
    lst.append(number[N % B])
    N //= B

lst.reverse()
rslt = []
rslt = ''.join(lst)
print(rslt)