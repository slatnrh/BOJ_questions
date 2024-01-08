n = int(input())

for _ in range(n):
    rslt = 1
    ratio = 1
    k = int(input())

    for i in range(1, k):
        ratio *= 2
        rslt += ratio
    
    print(rslt)