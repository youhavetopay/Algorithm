from collections import deque

def find_start_loc(maps):

    for y in range(len(maps)):
        for x in range(len(maps[0])):
            if maps[y][x] == 'S':
                return [x, y]

def check_length(max_x, max_y, x, y):
    if 0 <= x < max_x and 0 <= y < max_y:
        return True
    
    return False

def bfs(maps, start_loc, end):

    MAX_X = len(maps[0])
    MAX_Y = len(maps)

    queue = deque()

    queue.append(start_loc + [0])
    visited = set()
    visited.add((start_loc[0], start_loc[1]))

    vectors = [[0, 1], [0, -1], [1, 0], [-1, 0]]

    while queue:

        x, y, move = queue.popleft()

        if maps[y][x] == end:
            return [x, y, move]

        for dx, dy in vectors:
            next_x, next_y = x + dx, y + dy

            if check_length(MAX_X, MAX_Y, next_x, next_y) \
                and (next_x, next_y) not in visited \
                    and maps[next_y][next_x] != 'X':
                visited.add((next_x, next_y))
                queue.append([next_x, next_y, move + 1])

    return -1


def solution(maps):

    '''
        나의 풀이
        레버 위치에 갔다가 출구로 가면 탈출을 하는데
        탈출하는데 필요한 최소 이동거리를 구하는 문제

        나의 접근법
        처음엔 문제 잘못 이해하고 그냥 단순 BFS 문제인 줄 알았는데
        레버에 갔다가 가야 탈출에 성공한다는 걸 알고
        그냥 BFS 두번 함 ㅋㅋㅋ
        시작 -> 레버 최소 이동거리 + 레버 -> 출구 최소 이동거리
        이렇게 계산하면 풀림 ㅋㅋ

        개인적으로 이런 미로 탐색 문제가 좀 재밌음 ㅋㅋㅋㅋ
    '''

    lever_loc = bfs(maps, find_start_loc(maps), 'L')
    if lever_loc == -1:
        return -1
    
    exit_loc = bfs(maps, lever_loc[:-1], 'E')

    if exit_loc == -1:
        return -1


    return exit_loc[-1] + lever_loc[-1]

print(solution(["SOOOL","XXXXO","OOOOO","OXXXX","OOOOE"]))



def fast_way_bfs(maps, start, end):
    visited = [[0] * 1000 for _ in range(1000)]

    drs, dcs = [0, 0, 1, -1], [1, -1, 0, 0]
    queue = deque()
    queue.append(start)

    distance = 0
    while len(queue):
        r, c, dist = queue.popleft()
        if not (0 <= r < len(maps)) or not(0 <= c < len(maps[0])):
            continue
        if maps[r][c] == 'X' or visited[r][c] == True:
            continue
        if maps[r][c] == maps[end[0]][end[1]]:
            return dist
        
        visited[r][c] = True

        for dr, dc in zip(drs, dcs):
            if 0 <= r + dr < len(maps) and 0 <= c+dc < len(maps[0]):
                if maps[r+dr][c+dc] != 'X' and visited[r+dr][c+dc] == False:
                    queue.append((r+dr, c+dc, dist+1))

    return -1


def firstSolu(maps):

    '''
        다른 사람 풀이
        프로그래머스 다른 사람 풀이
        https://school.programmers.co.kr/learn/courses/30/lessons/159993/solution_groups?language=python3

        나랑 똑같은 풀이 ㅋㅋㅋ
        BFS 두번해서 나온 이동거리를 더해주는 방식
        문제 자체가 이해만 된다면..ㅋㅋㅋ 
        간단하게 풀리는 듯ㅋㅋㅋ
    '''
    
    start, lever, end = 0, 0, 0
    for r in range(len(maps)):
        for c in range(len(maps[0])):
            if maps[r][c] == 'S':
                start = r, c, 0
            if maps[r][c] == 'E':
                end = r, c, 0
            if maps[r][c] == 'L':
                lever = r, c, 0
    
    first, second = fast_way_bfs(maps, start, lever), fast_way_bfs(maps, lever, end)
    if -1 in [first, second]:
        return -1
    
    return first + second