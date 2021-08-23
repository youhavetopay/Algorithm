# # 토마토
from collections import deque

n, m = map(int, input().split())


board = []
checkBoard = []
xMove = [1, -1 , 0, 0]
yMove = [0, 0, 1, -1]

queue = deque()

def check(x,y):
    global n, m
    return 0<= x <n and 0<= y <m

tempQueue = []
for y in range(m):
    tempBoard = list(map(int, input().split()))
    tempCheck = [False] * n

    for x, v in enumerate(tempBoard):
        if v == 1:
            tempQueue.append([x, y])
    
    board.append(tempBoard)
    checkBoard.append(tempCheck)

if tempQueue != []:
    queue.append(tempQueue)
    day = -1

    while True:

        tempQueue = []

        for nowLoc in list(queue.popleft()):
            board[nowLoc[1]][nowLoc[0]] = 1
            
            for i in range(4):
                nextX = nowLoc[0]+xMove[i]
                nextY = nowLoc[1]+yMove[i]
                
                if check(nextX, nextY):
                    if board[nextY][nextX] == 0 and checkBoard[nextY][nextX] == False:
                        
                        tempQueue.append([nextX, nextY])
                        checkBoard[nextY][nextX] = True
            
        queue.append(tempQueue)
        
        day += 1

        if tempQueue == []:
            break     

    for tempBoard in board:
        if 0 in tempBoard:
            print(-1)
            break
    else:
        print(day)
        
else:
    print(-1)
