import sys
input = sys.stdin.readline

# dfs
def dfs(start):
    visited[start] = True
    virus_com.append(start)

    for i in graph[start]:
        if not visited[i]:
            dfs(i)

computer = int(input())
line = int(input())
graph = [[] for _ in range(computer+1)]

for _ in range(line):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (computer+1)
virus_com = []

# 1번 컴퓨터에서 시작하여 연결된 모든 컴퓨터 감염
dfs(1)
# -1의 이유: 1번 컴퓨터를 제외한 감염된 컴퓨터 출력
print(len(virus_com)-1)