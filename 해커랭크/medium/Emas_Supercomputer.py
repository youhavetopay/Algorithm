

def findCross(maxN, maxM, grid, centerN, centerM):
    blockCount = 1
    
    while True:
        flag = 0
        if 0<= centerN + blockCount < maxN and grid[centerN + blockCount][centerM] == 'G':
            flag += 1
        if 0<= centerN - blockCount < maxN and grid[centerN - blockCount][centerM] == 'G':
            flag += 1
        if 0<= centerM + blockCount < maxM and grid[centerN][centerM + blockCount] == 'G':
            flag += 1
        if 0<= centerM - blockCount < maxM and grid[centerN][centerM - blockCount] == 'G':
            flag += 1
        
        if flag != 4:
            return blockCount-1
        else:
            blockCount += 1

def twoPluses(n, m, N, M,grid, queue):
    # Write your code here
    answer = 1

    if len(queue) == 2:
        print('기저')
        for temp in queue:
            answer *= temp
        return answer

    for index1 in range(N, n): #n
        for index2 in range(M, m): # m
            sumBlock = 0
            if grid[index1][index2] == 'G':
                crossLength = findCross(n, m, grid, index1, index2)
                sumBlock = 1 + (crossLength * 4)
                print('a전', index1, index2)
                a = twoPluses(n, m, index1,index2+1,grid, queue)
                print('a끝-----------', index1, index2)
                print(queue)
                print(grid)

                print('-------------------------')
                tempGrid = grid.copy()

                for i in range(crossLength+1):
                    print('원영이인성')
                    tempGrid[index1+i][index2] = 'B'
                    tempGrid[index1-i][index2] = 'B'
                    tempGrid[index1][index2+i] = 'B'
                    tempGrid[index1][index2-i] = 'B'
                print(tempGrid[index1][index2],'----' ,index1, index2)
                tempQueue = queue.copy()
                tempQueue.append(sumBlock)
                

                print(tempQueue)
                print(tempGrid)
                
                b = twoPluses(n, m, index1, index2+1, tempGrid, tempQueue)
                print('b끝-----------')
                print(a,b)
                answer = max(a,b)

                
    return answer

n1 = 6
m1 = 7
g1 = [ 
'GGGGGGG',
'BGBBBBG',
'BGBBBBG',
'GGGGGGG',
'GGGGGGG',
'BGBBBBG'
]

n2 = 8
m2 = 8
g2 = [
    ['G','G','G','G','G','G','G','G'],
    ['G','B','G','B','G','G','B','G'],
    ['G','B','G','B','G','G','B','G'],
    ['G','G','G','G','G','G','G','G'],
    ['G','B','G','B','G','G','B','G'],
    ['G','G','G','G','G','G','G','G'],
    ['G','B','G','B','G','G','B','G'],
    ['G','G','G','G','G','G','G','G']
]

print(twoPluses(n2, m2, 0,0,g2, []))