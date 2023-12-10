from collections import deque
 
T = int(input())
 
for i in range(T):
    p = input()
    n = int(input())
    # 괄호 없애주기 위해 slicing
    x = input()[1:-1].split(',')
 
    queue = deque(x)

    flag = 0
    if n == 0:
        queue = []
 
    for function in p:
        if function == 'R':
            flag += 1
        elif function == 'D':
            if len(queue) == 0:
                print("error")
                break
            else:
                # flag가 짝수일 경우 기존 array 상태 -> popleft
                if flag % 2 == 0:
                    queue.popleft()
                # flag가 홀수일 경우 reverse 상태 -> pop
                else:
                    queue.pop()
 
    else:
        if flag % 2 == 0:
            print("[" + ",".join(queue) + "]")
        else:
            queue.reverse()
            print("[" + ",".join(queue) + "]")