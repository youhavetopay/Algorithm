# 단지번호붙이기

import sys
def DFS(x,y):
    stack = [[x,y]]
    edgeCount = 0
    global board
    while True:
        
        temp = stack[-1]
        edgeCount += 1
        
        board[temp[0]] = board[temp[0]][0:temp[1]] +'0'+board[temp[0]][temp[1]+1:]
        
        # 오른쪽
        if temp[0] + 1 < N and board[temp[0] + 1][temp[1]] == '1' and [temp[0] + 1, temp[1]] not in stack:
            stack.append([temp[0] + 1, temp[1]])
        
        # 왼쪽
        if temp[0] - 1 >= 0 and board[temp[0] - 1][temp[1]] == '1' and [temp[0] - 1, temp[1]] not in stack:
            stack.append([temp[0] - 1, temp[1]])
        
        # 아래
        if temp[1] + 1 < N and board[temp[0]][temp[1] + 1] == '1' and [temp[0], temp[1] + 1] not in stack:
            stack.append([temp[0], temp[1] + 1])
        
        # 위
        if temp[1] - 1 >= 0 and board[temp[0]][temp[1]-1] == '1' and [temp[0], temp[1] - 1] not in stack:
            stack.append([temp[0], temp[1] - 1])
        
        stack.remove(temp)
        if len(stack) == 0:
            break

    return edgeCount
        
        

N = int(sys.stdin.readline())
board = []

for i in range(N):
    temp = sys.stdin.readline()
    board.append(temp[:-1])

stack = []
answer = []

for index in range(N):
    for index2 in range(N):
        if board[index][index2] == '1':
            count = DFS(index, index2)
            answer.append(count)
            
            continue
            
print(len(answer))
answer.sort()
for i in answer:
    print(i)