import sys
input = sys.stdin.readline

M = int(input())
num_set = set()

for _ in range(M):
    command = input().strip().split()
    
    if len(command) == 1:
        if command[0] == "all":
            num_set = set([i for i in range(1, 21)])
        else:
            num_set = set()
    
    else:
        func, x = command[0], command[1]
        x = int(x)

        if func == "add":
            num_set.add(x)
        elif func == "remove":
            num_set.discard(x)
        elif func == "check":
            print(1 if x in num_set else 0)
        elif func == "toggle":
            if x in num_set:
                num_set.discard(x)
            else:
                num_set.add(x)