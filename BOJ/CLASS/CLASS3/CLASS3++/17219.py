import sys
input = sys.stdin.readline

N, M = map(int, input().split(' '))

page_info = {}

for _ in range(N):
    page, password = map(str, input().strip().split(' '))
    page_info[page] = password

for _ in range(M):
    page = input().strip()
    print(page_info[page])
