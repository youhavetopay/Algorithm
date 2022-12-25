from collections import deque

def checkPosition(nextX, nextY, maxSize, grid):
    if 0 <= nextX < maxSize and 0 <= nextY < maxSize:
        if grid[nextX][nextY] == '.':
            return True
    
    return False

def getMoveVector(x, y, max_size, grid):

    move_vec = [[0, 1], [0, -1], [1, 0], [-1, 0]]

    vec_list = []

    for vec in move_vec:
        next_x, next_y = x + vec[0], y + vec[1]

        # 한번에 갈 수 있는 행 혹은 열을 전부 담아주기
        while checkPosition(next_x, next_y, max_size, grid): 
            vec_list.append([next_x, next_y])
            next_x, next_y = next_x + vec[0], next_y + vec[1]

    return vec_list


def minimumMoves(grid, startX, startY, goalX, goalY):
    # Write your code here
    
    max_size = len(grid)
    
    queue = deque([[startX, startY, 0]])
    visit = set() # set이 단순 List보다 in 할때 시간복잡도가 빠름 -> hash로 되어 있어서?

    while len(queue) > 0:
        x, y, now_vec = queue.popleft()
        
        now_vec += 1

        # 이번에 갈 수 있는 위치들 전부 가져오기
        vector_list = getMoveVector(x, y, max_size, grid)
        for vector in vector_list:
            next_x, next_y = vector[0], vector[1]

            if next_x == goalX and next_y == goalY:
                return now_vec

            if (next_x, next_y) not in visit:
                queue.append([next_x, next_y, now_vec])
                visit.add((next_x, next_y))

    return -1


# g1 = ['.X.', '.X.', '...']

# g1 = [
#     '.X..XX...X',
#     'X.........',
#     '.X.......X',
#     '..........',
#     '........X.',
#     '.X...xxx..',
#     '.....X..XX',
#     '.....X.X..',
#     '..........',
#     '.....X..XX'
# ]

g1 = [
    '.......',
    '.......',
    '.......',
    '.......',
    '.......',
    '.......',
    '...x...',
]

#print(minimumMoves(g1, 0, 0, 2, 2))
print(minimumMoves(g1, 6, 0, 6, 6))