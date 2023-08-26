
import sys
input = sys.stdin.readline

from collections import deque

N = int(input())

board = []

end = [-1, -1]

for y in range(N):
    row = list(input().rstrip())

    if end[0] == -1:
        for i, word in enumerate(row):
            if word == 'F':
                end = [i, y]
                break

    board.append(row)

direction = [
    [-1, -1], [0, -1], [1, -1],
    [-1, 0], [1, 0],
    [-1, 1], [1, 1]
]


queue = deque()
answer = 0
queue.append((end[0], end[1]))

while queue:

    now_x, now_y = queue.popleft()

    for dx, dy in direction:
        nx, ny = now_x + dx, now_y + dy
        if 0 <= nx < N and 0 <= ny < N and board[ny][nx] == '.':
            answer += 1
            board[ny][nx] = '-1'
            queue.append((nx, ny))

print(answer)