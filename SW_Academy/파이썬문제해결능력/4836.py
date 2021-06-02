# 색칠하기


T = int(input())

for test_case in range(1, T+1):
    board = [[0 for _ in range(10)] for _ in range(10)]
    boxCount = int(input())
    
    redBoxInfo = []
    blueBoxInfo = []

    for i in range(boxCount):
        tempList = list(map(int, input().split()))
        if tempList[-1] == 1:
            redBoxInfo.append(tempList)
        else:
            blueBoxInfo.append(tempList)

    
    for box in redBoxInfo:
        for x in range(box[0], box[2]+1):
            for y in range(box[1], box[3]+1):
                board[x][y] = 1
    
    answer = 0
    for box in blueBoxInfo:
        for x in range(box[0], box[2]+1):
            for y in range(box[1], box[3]+1):
                if board[x][y] == 1:
                    answer += 1
    
    print('#'+str(test_case), answer)

    
