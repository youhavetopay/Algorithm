# 미로찾기

n, m = map(int, input().split())

board = []
checkList = []
for _ in range(n):
    tempList = list(input())
    tempList2 = [False] * m
    board.append(tempList)
    checkList.append(tempList2)


queue = [[0,0,1]]

nowLoc = [0,0,1]

checkList[nowLoc[1]][nowLoc[0]] = True

while True:

    nowLoc = queue.pop(0)

    # 오른쪽
    if nowLoc[0] + 1 <= m - 1 and board[nowLoc[1]][nowLoc[0]+1] != '0':
        if not checkList[nowLoc[1]][nowLoc[0] + 1]:

            queue.append([nowLoc[0]+1, nowLoc[1], nowLoc[2] + 1])
            checkList[nowLoc[1]][nowLoc[0]+1] = True

            if board[nowLoc[1]][nowLoc[0]+1] == '1':
                board[nowLoc[1]][nowLoc[0]+1] = nowLoc[2] + 1
    
    # 왼쪽
    if nowLoc[0] - 1 >= 0 and board[nowLoc[1]][nowLoc[0]-1] != '0':
        if not checkList[nowLoc[1]][nowLoc[0] - 1]:
            
            queue.append([nowLoc[0]-1, nowLoc[1], nowLoc[2] + 1])
            checkList[nowLoc[1]][nowLoc[0]-1] = True

            if board[nowLoc[1]][nowLoc[0]-1] == '1':
                board[nowLoc[1]][nowLoc[0]-1] = nowLoc[2] + 1

    # 아래  왼쪽 위에서 오른쪽 아래로 가는거라서
    if nowLoc[1] + 1 <= n- 1 and board[nowLoc[1]+1][nowLoc[0]] != '0':
        if not checkList[nowLoc[1] + 1][nowLoc[0]]:

            queue.append([nowLoc[0], nowLoc[1] + 1, nowLoc[2]+ 1])
            checkList[nowLoc[1]+1][nowLoc[0]] = True

            if board[nowLoc[1]+1][nowLoc[0]] == '1':
                board[nowLoc[1]+1][nowLoc[0]] = nowLoc[2] + 1

    # 위
    if nowLoc[1] - 1 >= 0 and board[nowLoc[1]-1][nowLoc[0]] != '0':
        if not checkList[nowLoc[1] - 1][nowLoc[0]]:

            queue.append([nowLoc[0], nowLoc[1] - 1, nowLoc[2]+ 1])
            checkList[nowLoc[1]-1][nowLoc[0]] = True
            
            if board[nowLoc[1]-1][nowLoc[0]] == '1':
                board[nowLoc[1]-1][nowLoc[0]] = nowLoc[2] + 1
    print()
    for temp in board:
        print(temp)

    if board[n-1][m-1] != '1':
        break
    

print(board[n-1][m-1])