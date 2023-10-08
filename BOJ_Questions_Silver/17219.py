import sys
input = sys.stdin.readline

N, M = map(int, input().split())

site_list = dict()
for _ in range(N):
    site, password = input().split()
    site_list[site] = password

for _ in range(M):
    explore_site = input().strip()
    print(site_list[explore_site])