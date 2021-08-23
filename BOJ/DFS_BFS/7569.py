# 토마토 3차원 버전 ㅋㅋ

from collections import deque
import sys
m, n, h = map(int, sys.stdin.readline().split())

board = []
queue = deque()

xMove = [1,-1,0,0,0,0]
yMove = [0,0,1,-1,0,0]
zMove = [0,0,0,0,1,-1]

for z in range(h):
    tempBoard = []

    for y in range(n):
        tempBoard.append(list(map(int, sys.stdin.readline().split())))
        for x, v in enumerate(tempBoard[-1]):
            if v == 1:
                queue.append([x,y,z])

    board.append(tempBoard)

if list(queue) == []:
    print(-1)

else:
    lastLoc = []

    while queue:

        nowLoc = queue.popleft()
        lastLoc = nowLoc

        for x,y,z in zip(xMove, yMove, zMove):
            nextX = nowLoc[0] + x
            nextY = nowLoc[1] + y
            nextZ = nowLoc[2] + z
        
            if 0<= nextX < m and 0<= nextY < n and 0<= nextZ < h:
                if board[nextZ][nextY][nextX] == 0:
                    queue.append([nextX,nextY,nextZ])
                    board[nextZ][nextY][nextX] = board[nowLoc[2]][nowLoc[1]][nowLoc[0]] + 1

    flag = 0
    for z in board:
        for y in z:
            if 0 in y:
                flag = 1
                break
        if flag == 1:
            break
    
    if flag == 1:
        print(-1)
    else:
        print(board[lastLoc[2]][lastLoc[1]][lastLoc[0]]-1)


# import sys
# from collections import deque
# m,n,h = map(int,input().split()) # mn크기, h상자수
# graph = []
# queue = deque([])
 
# for i in range(h):
#     tmp = []
#     for j in range(n):
#         tmp.append(list(map(int,sys.stdin.readline().split())))
#         for k in range(m):
#             if tmp[j][k]==1:
#                 queue.append([i,j,k])
#     graph.append(tmp)
    
# dx = [-1,1,0,0,0,0]
# dy = [0,0,1,-1,0,0]
# dz = [0,0,0,0,1,-1]
# while(queue):
#     x,y,z = queue.popleft()
    
#     for i in range(6):
#         a = x+dx[i]
#         b = y+dy[i]
#         c = z+dz[i]
#         if 0<=a<h and 0<=b<n and 0<=c<m and graph[a][b][c]==0:
#             queue.append([a,b,c])
#             graph[a][b][c] = graph[x][y][z]+1
            
# day = 0
# for i in graph:
#     for j in i:
#         for k in j:
#             if k==0:
#                 print(-1)
#                 exit(0)
#         day = max(day,max(j))
# print(day-1)