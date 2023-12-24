from collections import deque
import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    A, B = map(int, input().split())

    queue = deque()
    queue.append([A, ''])
    visited = [False for i in range(10001)]
    visited[A] = True

    while queue:
        num, command = queue.popleft()

        if num == B:
            print(command)
            break
        
        # D: D 는 n을 두 배로 바꾼다.
        # 결과 값이 9999 보다 큰 경우에는 10000 으로 나눈 나머지를 취한다.
        # 그 결과 값(2n mod 10000)을 레지스터에 저장한다.
        D = (num * 2) % 10000
        if not visited[D]:
            visited[D] = True
            queue.append([D, command + 'D'])
        # S: S 는 n에서 1 을 뺀 결과 n-1을 레지스터에 저장한다.
        # n이 0 이라면 9999 가 대신 레지스터에 저장된다.
        S = (num - 1) % 10000
        if not visited[S]:
            visited[S] = True
            queue.append([S, command + 'S'])
        # L: L 은 n의 각 자릿수를 왼편으로 회전시켜 그 결과를 레지스터에 저장한다.
        # 이 연산이 끝나면 레지스터에 저장된 네 자릿수는 왼편부터 d2, d3, d4, d1이 된다.
        L = num // 1000 + (num % 1000) * 10
        if not visited[L]:
            visited[L] = True
            queue.append([L, command + 'L'])
        # R: R 은 n의 각 자릿수를 오른편으로 회전시켜 그 결과를 레지스터에 저장한다.
        # 이 연산이 끝나면 레지스터에 저장된 네 자릿수는 왼편부터 d4, d1, d2, d3이 된다.
        R = num // 10 + (num % 10) * 1000
        if not visited[R]:
            visited[R] = True
            queue.append([R, command + 'R'])