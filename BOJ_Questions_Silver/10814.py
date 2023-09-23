import sys

n = int(sys.stdin.readline())
member_lst = []

for i in range(n):
    age, name = sys.stdin.readline().split()
    age = int(age)
    member_lst.append((age, name))

member_lst.sort(key = lambda x : x[0])

for i in member_lst:
    print(i[0], i[1])