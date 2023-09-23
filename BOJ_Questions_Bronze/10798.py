A = []
for row in range(5):
    row = input()
    A.append(row)

for j in range(15):
    for i in range(5):
        if(j < len(A[i])):
            print(A[i][j], end = '')