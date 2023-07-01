from collections import defaultdict

def solution(grid):

    '''
        나의 풀이
        빛을 보냈을때 다시 돌아오는 경로의 길이들을 구하는 문제

        나의 접근법
        걍 모든 노드에서 4방향으로 보내면서 체크함 ㅋㅋㅋ
        너무 효율성 생각안하고 막 해버림 ㅋㅋㅋㅋ

        그래도 그냥 단순히 모든 노드의 4방향에서 해버리면
        시간초과가 뜨기 때문에 한번 갔던 경로는 체크 안하도록 해야함 -> 한번 갔던 경로로 들어가면 결국 같은 경로기 때문
        그렇게 했더니 좀 아슬아슬하게 통과함 ㅋㅋㅋ

        2레벨 치곤 꽤 힘들었음 ㅠㅠ (거의 1시간 30분?? ㄷㄷ)
        내가 접근을 이상하게 한 걸 수도 있지만..

        그래도 예전에 월간 코드 챌린지 참여했을 때는 
        엄두도 못냈는데 지금은 시간이 좀 걸리더라도 풀었다는게
        정말 많이 성장한걸 느낌 ㅎㅎ
    '''

    answer = []

    # 돌아오는 경로에 포함되는 길? 모음 (중복 방문 방지용)
    visited = set()
    # 길이별 루트
    total_routes = defaultdict(set)

    # 모든 노드 검사
    for y in range(len(grid)):
        for x in range(len(grid[0])):

            # 해당 노드에서 시작된 루트 가져오기
            routes = find_route([x, y], grid, visited)
            
            # 루트들을 중복되지 않게 길이별로 넣어주기
            for length, now_routes in routes.items():
                for route in now_routes:
                    total_routes[length].add(route)

    # 길이별로 정렬해서 정답에 넣어주기
    for length in sorted(total_routes.keys()):
        for i in range(len(total_routes[length])):
            answer.append(length)

    return answer

def find_route(start, grid, total_visited):

    # 시작점
    now = start
    # 길이별 루트
    total_routes = defaultdict(set)

    # 이동 방향
    vectors = [[0, 1], [0, -1], [1, 0], [-1, 0]]

    for arrow, (dx, dy) in enumerate(vectors):
        next_x, next_y = now[0] + dx, now[1] + dy

        # 리스트의 길이를 넘어가면 반대쪽에서 와야해서 별도로 체크
        next_x, next_y = get_next_loc(next_x, next_y, grid)

        # 시작 방향
        start_info = (next_x, next_y, arrow)

        # 방문했던 곳들
        visited = set()
        now_arrow = arrow

        # 방문했던 노드로 다시 돌아오기 전까지 반복
        while (next_x, next_y, now_arrow) not in visited and (next_x, next_y, now_arrow) not in total_visited:
            
            # 이동 경로 넣어주기
            visited.add((next_x, next_y, now_arrow))

            x, y = next_x, next_y
            
            # 다음 방향 구하기
            next_arrow = get_arrow(now_arrow, grid[y][x])
            next_dx, next_dy = vectors[next_arrow]

            next_x, next_y = get_next_loc(x + next_dx, y + next_dy, grid)
            now_arrow = next_arrow

            # 시작했던 곳으로 돌아왔을 경우
            if (next_x, next_y, now_arrow) == start_info:
                visited.add(True)
                break
        
        # 시작했던 곳으로 돌아오는 경로 일 경우
        if True in visited:
            visited.remove(True)

            # 경로 넣어주기
            for route in visited:
                total_visited.add(route)
            temp = sorted(list(visited), key=lambda x:(x[0], x[1], x[2]))
            total_routes[len(temp)].add(' '.join(map(str, temp)))
                    
    return total_routes

def get_next_loc(x, y, grid):
    if x < 0:
        x = len(grid[0]) - 1
    elif x >= len(grid[0]):
        x = 0
    
    if y < 0:
        y = len(grid) - 1
    elif y >= len(grid):
        y = 0

    return x, y

def get_arrow(now_arrow, grid):

    next_arrow = None
    if grid == 'L':
        next_arrow = get_arrow_by_grid_L(now_arrow)
    elif grid == 'R':
        next_arrow = get_arrow_by_grid_R(now_arrow)
    else:
        next_arrow = now_arrow
    
    return next_arrow

def get_arrow_by_grid_L(now_arrow):

    # 위에서 옴
    if now_arrow == 0:
        return 2
    
    # 아래에서 옴
    elif now_arrow == 1:
        return 3
    
    # 왼쪽에서 옴
    elif now_arrow == 2:
        return 1
    
    # 오른쪽에서 옴
    else:
        return 0

def get_arrow_by_grid_R(now_arrow):

    # 위에서 옴
    if now_arrow == 0:
        return 3
    
    # 아래에서 옴
    elif now_arrow == 1:
        return 2
    
    # 왼쪽에서 옴
    elif now_arrow == 2:
        return 0
    
    # 오른쪽에서 옴
    else:
        return 1
    

print(solution(["SL","LR"]))



def firstSolu(grid):

    '''
        다른 사람 풀이
        프로그래머스 다른 사람 풀이
        https://school.programmers.co.kr/learn/courses/30/lessons/86052/solution_groups?language=python3

        이 분도 모든 노드에서 체크를 했는데
        set으로 방문체크를 하는 것이 아닌 3차원 리스트로 체크함 -> 이게 더 깔끔한듯??

        또한 이동방향을 순서를 저렇게 해두니
        방향 체크하는게 훨씬 간단한듯 ㅋㅋㅋㅋㅋ
        
        접근법은 나랑 똑같지만
        사용한 자료구조??가 다른데 훨씬 깔끔하게 하신듯 함 ㅎㅎ
    '''

    R, C = len(grid), len(grid[0])

    dxy = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    grf = [[[0,0,0,0] for _ in range(C)] for _ in range(R)]

    def solve(x, y, d):
        res = 0
        while not grf[x][y][d]:
            grf[x][y][d] = 1
            x, y = (x + dxy[d][0]) % R, (y+dxy[d][1]) % C
            if grid[x][y] == 'L':
                d = (d + 1) % 4
            elif grid[x][y] == 'R':
                d = (d - 1) % 4
            
            res += 1
        
        return res
    
    ans = []
    for i in range(R):
        for j in range(C):
            for k in range(4):
                if grf[i][j][k] == 0:
                    ans.append(solve(i, j, k))

    return sorted(ans)