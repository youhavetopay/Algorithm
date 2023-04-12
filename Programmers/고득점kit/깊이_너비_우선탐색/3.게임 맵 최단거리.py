import collections

def solution(maps):

    '''
        나의 풀이
        미로 최단거리 찾는 문제

        역시 BFS 기본 문제라서 푸는 방법을 떠올리는데는
        어렵지 않았지만 여러가지 뻘짓을 많이해서 생각보다 오래걸림 ㅋㅋ
        방문체크 할려고 visited 리스트를 만들었는데 자꾸 이상하게 되서 
        아예 리스트 새로 할당하는 방식으로 만드니 정상 작동함 ㅋㅋㅋㅋ
    '''

    answer = 0

    # 처음 시작 위치
    queue = collections.deque([[[0, 0]]])

    max_width = len(maps[0])
    max_height = len(maps)

    # 방문 여부
    visited = [[False for _ in range(max_width)] for __ in range(max_height)]
    visited[0][0] = True

    vectors = [[1,0], [-1, 0], [0, 1], [0, -1]]

    move_dist = 1

    # BFS 시작
    while queue:

        now_locs = queue.popleft()
        
        next_locs = []

        for i, j in now_locs:
            maps[i][j] = move_dist
            
            # 갈 수 있는곳 넣어주기
            for x, y in vectors:
                if 0 <= (j + x) < max_width and 0 <= (i + y) < max_height \
                    and maps[i+y][j+x] == 1 and visited[i+y][j+x] == False:
                    next_locs.append([i + y, j + x])
                    visited[i+y][j+x] = True
                    
            
        if next_locs:
            queue.append(next_locs)
        
        move_dist += 1

    # 목적지까지 최단 거리
    answer = maps[max_height-1][max_width-1]

    # 방문한적이 없다면 갈 수 없는 곳
    # 입력에서 1 x 1 리스트는 주어지지 않는다고 했음
    if maps[max_height-1][max_width-1] == 1:
        answer = -1

    return answer


print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))


def firstSoul(maps):

    '''
        다른 사람 풀이
        https://jokerldg.github.io/algorithm/2021/05/23/game-map.html

        BFS 기본 문제라서 그런지 왠만한 풀이 전부다 BFS로 푸신듯??
        근데 하는건 나랑 거의 똑같은데 코드는 웰케 깔끔해보이지?? ㅋㅋㅋㅋㅋ

        차이점이라면 이동 거리를 체크하는 리스트를 따로 만들어서
        -1 로 초기화 해둔 점??
    '''

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    r = len(maps)
    c = len(maps[0])

    graph = [[-1 for _ in range(c)] for _ in range(r)]

    queue = collections.deque()
    queue.append([0, 0])

    graph[0][0] = 1

    while queue:
        y, x = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= ny < r and 0 <= nx < c and maps[ny][nx] == 1:
                if graph[ny][nx] == -1:
                    graph[ny][nx] = graph[y][x] + 1
                    queue.append([ny, nx])
    
    answer = graph[-1][-1]

    return answer