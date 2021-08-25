# 나이트의 이동

from collections import deque

test_case = int(input())

moveVector = [
    [-1, 2], [-2, 1], 
    [-2, -1], [-1, -2],
    [1, -2], [2, -1],
    [2, 1], [1, 2]
]

for tc in range(test_case):

    boardLenght = int(input())

    board = [ [ 0 for _ in range(boardLenght)] for _ in range(boardLenght)]

    nowLoc = list(map(int, input().split()))

    objectLoc = list(map(int, input().split()))

    queue = deque()

    if nowLoc == objectLoc:
        print(0)
        continue
    
    queue.append(nowLoc)

    while queue:

        nowLoc = queue.popleft()

        if nowLoc == objectLoc:
            print(board[nowLoc[1]][nowLoc[0]])
            break

        for vector in moveVector:

            nextX = nowLoc[0]+vector[0]
            nextY = nowLoc[1]+vector[1]

            if 0<= nextX <boardLenght and 0 <= nextY < boardLenght:
                
                if board[nextY][nextX] == 0:
                    board[nextY][nextX] = board[nowLoc[1]][nowLoc[0]] + 1
                    
                    queue.append([nextX, nextY])
        
        # for t in board:
        #     print(t)


