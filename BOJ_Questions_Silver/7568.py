import sys

N = int(sys.stdin.readline())
student_lst = []

for _ in range(N):
    weight, height = map(int, sys.stdin.readline().split())
    student_lst.append((weight, height))

lst = []
for i in student_lst:
    grade = 1
    for j in student_lst:
        if i[0] < j[0] and i[1] < j[1]:
            grade += 1
    lst.append(grade)

for i in range(N):
    print(lst[i], end = ' ')