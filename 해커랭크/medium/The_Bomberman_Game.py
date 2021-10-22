def checkRow(maxRow, value):
    if 0 <= value < maxRow:
        return True
    return False

def checkColum(maxCol, value):
    if 0 <= value < maxCol:
        return True
    return False

def bomberMan(r, c,n, grid):
    # Write your code here
    
    sec = 1
    
    ListGrid = []
    for temp in grid:
        ListGrid.append(list(temp))
    
    if n == 1:
        return grid
    
    if n % 2 == 0:
        for i in range(r):
            grid[i] = 'O' * c
        return grid
    
    if (n - 3) % 4 == 0:  # 최적화하기  반복된 패턴 있으니 잘 파악하기
        n = 3
    elif (n - 5) % 4 == 0:
        n = 5

    
    while sec < n:
        
        bombLocs = []
        # Find bomb Location
        for index1, values in enumerate(ListGrid): # r
            for index2, value in enumerate(values): # c
                if value == 'O':
                    bombLocs.append([index1, index2])
        
        # 1 notting
        # 1 ~ 2 second 
        for i in range(r):
            ListGrid[i] = ['O']*c
        sec += 1
        if sec >= n:
            break
        # print(bombLocs)
        # for temp in ListGrid:
        #     print(temp)
        # print()
        # 3 second
        for bomb in bombLocs:
            ListGrid[bomb[0]][bomb[1]] = '.'
            if checkRow(r, bomb[0]) and checkColum(c, bomb[1]+1):
                ListGrid[bomb[0]][bomb[1]+1] = '.'
            if checkRow(r, bomb[0]) and checkColum(c, bomb[1]-1):
                ListGrid[bomb[0]][bomb[1]-1] = '.'
            if checkRow(r, bomb[0]-1) and checkColum(c, bomb[1]):
                ListGrid[bomb[0]-1][bomb[1]] = '.'
            if checkRow(r, bomb[0]+1) and checkColum(c, bomb[1]):
                ListGrid[bomb[0]+1][bomb[1]] = '.'
            # for temp in ListGrid:
            #     print(temp)
            # print()
        sec += 1
        if sec >= n:
            break
    
    answer = []
    for temp in ListGrid:
        answer.append(''.join(temp))
    return answer

