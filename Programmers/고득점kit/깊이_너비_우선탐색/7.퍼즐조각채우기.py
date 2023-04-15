import collections



vec = [[0, 1], [0, -1], [1, 0], [-1, 0]]

def bfs(board, x, y, blocks, check_value):
    
    queue = collections.deque()
    queue.append([x, y])
    length = len(board)

    block = [[x, y]]
    board[y][x] = -1

    while queue:

        now_x, now_y = queue.popleft()

        for dx, dy in vec:
            next_x, next_y = now_x + dx, now_y + dy
            if 0 <= next_x < length and 0 <= next_y < length and\
                board[next_y][next_x] == check_value:
                board[next_y][next_x] = -1
                block.append([next_x, next_y])
                queue.append([next_x, next_y])
    
    for now_x, now_y in block:
        board[now_y][now_x] = len(block)

    blocks[len(block)].append(block[:])

    return

def makeBlocks(board, blocks, check_value):

    for y, line in enumerate(board):
        for x, value in enumerate(line):
            if value == check_value:
                bfs(board, x, y, blocks, check_value)
            elif check_value == 0 and value == 1:
                board[y][x] = -1
            

# 좌표값을 2차원 리스트로 만드는 함수
def normalizeBlock(block):

    # 빈공간 없이 왼쪽 상단에 블록을 붙여야 함

    # x 값을 기준으로 정렬
    block.sort(key=lambda x: x[0])

    # 가장 작은 값을 기준으로
    # 해당 x값 만큼 이동시키기
    point = block[0][0]
    for i in range(len(block)):
        block[i][0] -= point

    # 2차원 리스트의 너비
    max_widht = block[-1][0]

    # y 값을 기준으로 정렬
    block.sort(key=lambda x: x[1])

    # 가장 작은 값을 기준으로
    # 해당 y값 만큼 이동시키기
    point = block[0][1]
    for i in range(len(block)):
        block[i][1] -= point

    # 2차원 리스트의 높이
    max_height = block[-1][1]
    # 2차원 리스트 만들어주기
    board = [[0 for _ in range(max_widht+1)] for _ in range(max_height+1)] 

    # 좌표값에 해당하는 위치에 1로 표시해주기
    for x, y in block:
        board[y][x] = 1
    
    for t in board:
        print(t)
    
    print()
    
    return board

def doRightlotationBlock(block):

    # 블록 오른쪽으로 회전시키기
    temp = [[0 for _ in range(len(block))] for _ in range(len(block[0]))]
    for i in range(len(block[0])):
        for j in range(len(block)-1, -1, -1):
            temp[i][len(block)-j - 1] = block[j][i]


    return temp

def checkBlock(blank_block, block):

    # 블록을 오른쪽으로 4번 돌리면서 체크하기
    for i in range(4):
        if blank_block == block: # 빈칸이랑 블록이 일치하면 성공
            return True
        print(blank_block, block)

        # 블록 오른쪽으로 돌리기
        block = doRightlotationBlock(block)
        
    
    return False


def solution(game_board, table):

    '''
        나의 풀이..... (진짜 미친.... 3시간 걸림..ㅋㅋㅋ)

        퍼즐 조각을 채워서 가장 많이 채우는 개수를 구하는 문제..

        나의 접근법.. ㅋ
        일단 BFS로 블록의 위치들을 칸의 개수 만큼 담아둠(빈공간, 블럭 따로따로)
        그 후 빈공간의 들의 칸의 수를 정렬해서 2칸짜리의 빈칸은 잘 계산해서 넣어주고
        3칸부터는 해당 칸을 가지는 블록을 돌려가면서 체크함
        그렇게 찾아감..

        이거 2020년 네이버 공채 4번 문제였던 것 같은데
        이걸 어떻게 + 3문제 해서 2시간만에 풀어ㅠㅠㅠㅠㅠㅠㅠ

        그래도 시간지나서 이렇게 풀어봤다는거에 의미를 둬야 할듯.. ㅋ
    '''

    answer = 0

    blank_blocks = collections.defaultdict(list)
    blocks = collections.defaultdict(list)
    
    # 빈칸이랑 블록 찾기 BFS
    # 해당 좌표값을 칸에 맡게 넣어줌
    makeBlocks(game_board, blank_blocks, 0)
    makeBlocks(table, blocks, 1)
    
    # 빈칸의 칸수를 정렬해서 칸 수가 작은거 부터 시작
    for block_count in sorted(list(blank_blocks.keys())):
        
        # 해당 칸수를 가지는 블록이 있는지 체크
        # 딱 들어가야 하므로
        if block_count in blocks:
            
            # 블록 칸의 2까지는 어떤 모양이든 간에 넣을 수 있음
            # 빈칸의 수만큼이나 가지고 있는거 만큼 더해주기
            if block_count <= 2:
                if len(blank_blocks[block_count]) <= len(blocks[block_count]):
                    answer += len(blank_blocks[block_count]) * block_count
                else:
                    answer += len(blocks[block_count]) * block_count
            else:

                # 이제 시작임.. ㅋㅋ
                # 해당 칸을 가지는 빈칸의 좌표 가져오기
                for blank_block in blank_blocks[block_count]:
                    
                    # 빈칸의 좌표값을 2차원 리스트로 만들기
                    normal_blank_block = normalizeBlock(blank_block)
                    
                    # 해당 칸을 가지는 블록의 좌표 가져오기
                    for i, block in enumerate(blocks[block_count]):
                        
                        # 블록의 좌표값을 2차원 리스트로 만들기
                        normal_block = normalizeBlock(block)
                        
                        # 들어가는지 확인하기
                        check_value = checkBlock(normal_blank_block, normal_block)
                        
                        # 들어가면 해당 블록 제거해주고 더해주기
                        # 그리고 다음 빈칸 확인하기
                        if check_value:
                            answer += block_count
                            blocks[block_count].pop(i)
                            break
        


    return answer

print(solution([
    [1,1,1,1,1,1],
    [1,0,0,0,1,1],
    [1,0,1,1,1,1],
    [1,1,1,1,1,1],
    [1,1,1,1,1,1],
    [1,1,1,1,1,1]
    ], 
               [
                    [0,0,0,0,0,0],
                    [0,0,0,0,0,0],
                    [0,1,1,0,0,0],
                    [0,0,1,0,0,0],
                    [0,0,1,0,0,0],
                    [0,0,0,0,0,0]
               ]
               ))



import itertools
import dataclasses

@dataclasses.dataclass(frozen=True)
class Pos:
    x: int
    y: int

    def neighbors(self):
        return [
            Pos(self.x, self.y - 1),
            Pos(self.x + 1, self.y),
            Pos(self.x, self.y + 1),
            Pos(self.x - 1, self.y)
        ]

def make_tile_form_positions(positions):

    def rotate90(tile):
        return tuple(
            tuple(tile[i][j] for i in range(len(tile)) for j in reversed(range(len(tile[0]))))
        )
    
    positions = set(positions)

    xs = [pos.x for pos in positions]
    min_x = min(xs)
    max_x = max(xs)

    ys = [pos.y for pos in positions]
    min_y = min(ys)
    max_y = max(ys)

    tile_representations = [
        tuple(
            tuple(Pos(i, j) in positions for j in range(min_y, max_y + 1) for i in range(min_x, max_x+1))
        )
    ]

    for __ in range(3):
        tile_representations.append(rotate90(tile_representations[-1]))
    
    return min(tile_representations)

def get_tile_size(tile):
    return sum(sum(row) for row in tile)

def parse_tiles(board, tile_value = 1):

    n = len(board)

    sentinel = 1 - tile_value
    board = [
        [sentinel] * (n + 2),
        *([sentinel] + row + [sentinel] for row in board),
        [sentinel] * (n + 2)
    ]

    tile_positions = []
    for i, j in itertools.product(range(1, n + 1), range(1, n + 1)):
        if board[i][j] == tile_value:
            stack = [Pos(i, j)]
            squares = []

            while stack:
                curr = stack.pop()
                board[curr.x][curr.y] = sentinel
                squares.append(curr)
                for neighbor in curr.neighbors():
                    if board[neighbor.x][neighbor.y] == tile_value:
                        stack.append(neighbor)
            
            tile_positions.append(squares)
    
    tiles = [make_tile_form_positions(p) for p in tile_positions]

    return tiles

def firstSoul(game_board, table):

    '''
        다른 사람 풀이
        프로그래머스 다른 사람 풀이

        문제가 많이 복잡한 문제였긴 하나봄.. ㅋㅋ
        프로그래머스에서 가장 좋아요가 많은 풀이인데 이정도이면.. ㅋㅋ

        근데 복잡해서 뭔소린지 1도 모르겠음... ㅠㅠ
    '''

    tiles = parse_tiles(table, 1)
    empty_spaces = parse_tiles(game_board, 0)

    tile_counter = collections.Counter(tiles)
    empty_space_counter = collections.Counter(empty_spaces)

    used_tiles = tile_counter & empty_space_counter

    return sum(get_tile_size(tile) * occ for tile, occ in used_tiles.items())