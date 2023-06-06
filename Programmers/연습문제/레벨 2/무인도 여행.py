from collections import deque

def check_lenght(max_x, max_y, x, y):
    if 0 <= x < max_x and 0 <= y < max_y:
        return True
    
    return False

def solution(maps):

    '''
        나의 풀이
        무인도의 개수에 따른 총 얻을 수 있는 식량을 구하는 문제

        나의 접근법
        그냥 그래프 개수 세는 문제나 마찬가지라서
        이중 for 문으로 탐색을 하면서 식량이 있고 방문을 안한 지점이라면
        BFS 를 해주는 방식으로 품

        BFS 기본 문제라서 어렵지 않았음
        개인적으로 BFS 문제가 조금 재밌는듯..???? ㅋㅋㅋㅋ
    '''

    answer = []

    visited = set()

    def bfs(x, y):
        queue = deque()

        MAX_X = len(maps[0])
        MAX_Y = len(maps)

        total_food = 0
        vectors = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        queue.append([x, y])
        visited.add((x, y))
        total_food += int(maps[y][x])

        while queue:

            now_x, now_y = queue.popleft()

            for dx, dy in vectors:
                next_x, next_y = now_x + dx, now_y + dy
                if check_lenght(MAX_X, MAX_Y, next_x, next_y) \
                    and maps[next_y][next_x] != 'X' \
                    and (next_x, next_y) not in visited:
                    total_food += int(maps[next_y][next_x])
                    visited.add((next_x, next_y))
                    queue.append([next_x, next_y])

        return total_food
    
    for y in range(len(maps)):
        for x in range(len(maps[0])):
            if maps[y][x] != 'X' and  (x, y) not in visited:
                answer.append(bfs(x, y))
    
    answer.sort()

    if len(answer) == 0:
        return [-1]

    return answer

print(solution(["X591X","X1X5X","X231X", "1XXX1"]))


def firstSolu(maps):

    '''
        다른 사람 풀이
        프로그래머스 다른 사람 풀이

        나랑 똑같은 풀이
        문제가 쉬워서 그런지 풀이법이 거기서 거긴듯 ㅋㅋ
    '''

    N, M = len(maps), len(maps[0])
    visited = [[0]* M for _ in range(N)]

    answer = []
    for i in range(N):
        for j in range(M):
            if maps[i][j] == 'X' or visited[i][j]:
                continue

            queue = deque()
            queue.append((i, j))
            visited[i][j] = 1
            n_food = int(maps[i][j])

            while queue:
                i0, j0 = queue.popleft()
                for di, dj in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                    ni, nj = i0+di, j0+dj
                    if 0 <= ni < N and 0 <= nj < M and not visited[ni][nj] and maps[ni][nj] != 'X':
                        queue.append((ni, nj))
                        visited[ni][nj] = 1
                        n_food += int(maps[ni][nj])
            
            answer.append(n_food)
    
    if not answer:
        answer.append(-1)
    else:
        answer.sort()
    
    return answer