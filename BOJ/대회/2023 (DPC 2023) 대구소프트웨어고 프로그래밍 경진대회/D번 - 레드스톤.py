import sys
from collections import deque
input = sys.stdin.readline


# W, H = map(int, input().split())
# N = int(input())
W, H = 19, 1
N = 19

board = [[''] * W for _ in range(H)]
energy = [[0] * W for _ in range(H)]

queue = deque()

lamps = []

temp = [['redstone_block', 0, 0],
['redstone_dust', 1, 0],
['redstone_dust', 2, 0],
['redstone_dust', 3, 0],
['redstone_dust', 4, 0],
['redstone_dust', 5, 0],
['redstone_dust', 18, 0],

['redstone_dust', 8, 0],
['redstone_dust', 9, 0],
['redstone_dust', 10, 0],
['redstone_dust', 11, 0],
['redstone_dust', 12, 0],
['redstone_dust', 13, 0],
['redstone_dust', 14, 0],
['redstone_dust', 15, 0],
['redstone_dust', 16, 0],
['redstone_dust', 17, 0],
['redstone_lamp', 18, 0]]
for idx in range(N):
    name, x, y = temp[idx]
    x = int(x)
    y = int(y)

    board[y][x] = name
    if name == 'redstone_block':
        queue.append([x, y, 15])
        energy[y][x] = 15

    elif name == 'redstone_lamp':
        lamps.append([x, y])

# for idx in range(N):
#     name, x, y = map(str, input().split())
#     x = int(x)
#     y = int(y)

#     board[y][x] = name
#     if name == 'redstone_block':
#         queue.append([x, y, 15])
#         energy[y][x] = 15

#     elif name == 'redstone_lamp':
#         lamps.append([x, y])

vectors = [(1, 0), (-1, 0), (0, 1), (0, -1)]
while queue:

    now_x, now_y, ele = queue.popleft()
    if ele == 1 and board[now_y][now_x] == 'redstone_dust':
        continue

    for dx, dy in vectors:
        next_x, next_y = now_x + dx, now_y + dy

        if 0 <= next_x < W and 0 <= next_y < H:

            if energy[next_y][next_x] < ele - 1 and board[next_y][next_x] != '':
                energy[next_y][next_x] = ele - 1
                queue.append([next_x, next_y, ele - 1])


flag = True
for x, y in lamps:
    if energy[y][x] == 0:
        print('failed')
        flag = False
        break

if flag:
    print('success')


