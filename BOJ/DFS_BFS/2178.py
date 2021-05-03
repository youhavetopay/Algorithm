# 미로찾기

import sys

N, M = map(int, sys.stdin.readline().split())

board = []

for i in range(N):
    board.append(str(sys.stdin.readline())[:-1])

print(board)