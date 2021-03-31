# 블록을 시계방향으로 90도 회전 하는 함수
def rotate(arr):
    # 90도 회전
    ret = [[-1 for _ in range(len(arr))] for _ in range(len(arr[0]))]

    for i in range(len(arr)):
        for j in range(len(arr[0])):
            ret[j][len(arr)-i-1] = arr[i][j]
    
    return ret

# 블록을 4개의 회전 형태를 만들고 이를 원점을 기준으로 상대 좌표의 목록으로 변환 ㄷㄷ
def generateRotations(inBlock):
    for rot in range(4):
        originY = -1
        originX = -1

        for i in range(len(inBlock)):
            for j in range(len(inBlock[0])):
                if inBlock[i][j] == 1:
                    if originY == -1:
                        # 가장 윗줄 맨 왼쪽에 있는 칸이 '원점'
                        originY = i
                        originX = j
                    
                    # 각 칸의 위치를 원점으로부터의 상대좌표로 표현
                    rotations[rot].append(i-originY, j-originX)
    
        inBlock = rotate(inBlock)

    # 4 가지의 회전 형태 중 중복이 있을 경우 이를 제거
    for i in range(4):
        for j in range(4):
            if i == j:
                continue
            if (not dup[i]) and (rotations[i] in rotations[j]):
                dup[j] = True

    #블록이 몇 칸짜리인지 저장
    blockSize = len(rotations[0])
 
# board의 (y,x)를 inType 방법으로 덮거나, 덮었던 블록을 없앤다.
# delta = 1 이면 덮고 , -1이면 덮었던 블록을 없앤다.

# 만약 블록이 제대로 덮이지 않는 경우 False 반환
# (게임판 밖으로 나갈때, 겹칠때, 검은칸을 덮을려고 할때)
def setFunction(y,x,inType, delta):
    ok = True
    rotation = rotations[inType]

    for i in range(len(rotation)):
        n = rotation
        ny = y + n[0]
        nx = x + n[1]
        if ny<0 or ny >= H or nx < 0 or nx >= W:
            ok = False
        elif ( board[ny][nx] += delta ) > 1:
            ok = False
    
    return ok

# placed : 지금까지 놓은 블록의 수
def search(placed):
    # 아직 채우지 못한 칸 중 가장 윗줄 왼쪽에 있는 칸을 찾음
    y, x = -1, -1

    for i in range(H):
        for j in range(W):
            if board[i][j] == 0:
                y = i
                x = j
                break

        if y != -1:
            break
    # 기저 사례 : 게임판의 모든 칸을 처리한 경우
    if y == -1:
        best = max(best, placed)
        return
    
    for typeValue in range(4):
        if dup[typeValue]:
            continue
        
        # 만약에 board[y][x]를 type형태로 덮을 수 있으면 재귀 호출
        if setFunction(y, x, typeValue, 1):
            search(placed+1)
        
        # 덮었던 블록을 치움
        setFunction(y, x, typeValue, -1)
    
    # 이 칸을 덮지 않고 막아두긴
    board[y][x] = 1
    search(placed)
    board[y][x] = 0

    return


rotations = [[],[],[],[]]
dup = [False, False, False, False]

H, W, R, C = int(input().split())

board = [[-1 for _ in range(inputValues[0])] for _ in range(inputValues[1])]
block = [[-1 for _ in range(inputValues[2])] for _ in range(inputValues[3])]

best = 0
blockSize = 0

for i in range(inputValues[1]):
    tempStr = input()
    for j in range(inputValues[0]):
        if tempStr[j] == '#':
            board[i][j] = 1
        else:
            board[i][j] = 0

for i in range(inputValues[3]):
    tempStr = input()
    for j in range(inputValues[2]):
        if tempStr[j] == '#':
            block[i][j] = 1
        else:
            block[i][j] = 0


generateRotations(block)
search(0)
print(best)