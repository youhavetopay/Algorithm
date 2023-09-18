
'''
    백준 2638. 치즈
    모든 치즈가 녹을때까지 걸리는 시간을 구하는 문제

'''

import sys
input = sys.stdin.readline

from collections import deque

def check_bfs(board, x, y, out_empty):

    N, M = len(board), len(board[0])

    visited = set()
    visited.add((x, y))

    q = deque()
    q.append((x, y))

    direction = ((1, 0), (-1, 0), (0, 1), (0, -1))

    while q:

        now_x, now_y = q.popleft()

        for dx, dy in direction:
            nx, ny = now_x + dx, now_y + dy

            # BFS를 하면서도 외부 공기 칸인지 체크해주기
            if (nx, ny) in out_empty:
                return True, visited

            # 칸을 넘어가는 경우는 외부 공기임
            if nx <= 0 or nx >= M-1 or ny <= 0 or ny >= N-1:
                return True, visited
            
            # 나머지 경우의 공기칸
            if 0 <= nx < M and 0 <= ny < N and board[ny][nx] == 0 and (nx, ny) not in visited:
                q.append((nx, ny))
                visited.add((nx, ny))

    # 칸을 넘어가지 않고 외부공기가 아니라면 내부 공기
    return False, visited




def solution():

    '''
        나의 풀이

        나의 접근법

        외부에 닿아있는 상하좌우가 두곳이상이면 해당 치즈가 녹고
        만약 내부 공기가 닿는 곳은 패스해야 하는데

        접근하는게 좀 어려웠음..

        그래서 생각한 방법이
        모든 치즈가 없어질때까지
        모든 board 를 탐색하면서 치즈를 찾고
        치즈가 있는 곳에서 BFS를 하는 방식으로 했는데 시간초과가 떴음..

        그래서 조금 최적화 한게 처음에 치즈 위치를 전부 찾아두고
        하나씩 빼면서 체크를 했는데도 시간초과.. 

        더 최적화 한게 BFS를 하면서 외벽에 닿으면 방문했던 공기칸은 외부 공기이기 때문에
        그것도 더해주면서 했는데 시간초과...

        도저히 모르겠어서 질문하기를 좀 봤는데
        예제 하나가 무한반복이 되길래 뭐지 싶어서 봤는데
        알고보니 BFS를 할때 방문 체크를 안하고 있어서 중복 방문 때문에
        시간초과가 떴었음.. ㅋㅋㅋㅋㅋㅋㅋㅋ

        실수 하나 때문에
        문제 푸는데 좀 오래걸림...

        다음부터는 꼼꼼히 살펴보자...ㅋ ㅋㅋㅋ
    '''

    board = []

    # N, M = map(int, input().split())

    

    N, M = 11, 15
    t = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0],
        [0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0],
        [0, 0, 1, 1, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0],
        [0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0],
        [0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
        [0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0],
        [0, 0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

    # N, M = 100, 100

    # t = [[1] * M for _ in range(N)]

    # 현재 남아있는 치즈들의 위치
    total_cheese = set()

    for y in range(N):
        # row = list(map(int, input().split()))
        row = t[y]
        board.append(row)

        # 치즈 위치 찾아주기
        for x in range(M):
            if row[x] == 1:
                total_cheese.add((x, y))
    

    direction = ((1, 0), (-1, 0), (0, 1), (0, -1))

    # 외부 공기들
    out_empty = set()

    print(total_cheese)

    answer = 0
    while total_cheese:

        remove_cheese = []

        for x, y in total_cheese:

            check = 0

            for dx, dy in direction:
                nx, ny = x + dx, y + dy

                # 칸이 넘어가는 경우면
                # 외부 공기랑 붙어있는거랑 마찬가지
                if nx <= 0 or nx >= M-1 or ny <= 0 or ny >= N-1:
                    check += 1
                    continue
                
                # 해당 칸이 외부 공기 일때
                if (nx, ny) in out_empty:
                    check += 1
                    continue
                
                # 위에 경우를 뺀 나머지 경우의 공기칸
                if 0 <= nx < M and 0 <= ny < N and board[ny][nx] == 0:
                    
                    # BFS해서 외부공기칸인지 아닌지 판별하기
                    check_value, visited = check_bfs(board, nx, ny, out_empty)

                    # 외부 공기라면 더해주기
                    if check_value:
                        out_empty = out_empty.union(visited)
                        check += 1
            
            # 외부 공기칸이랑 접하고 있는 칸이 2개 이상일때 없어짐
            if check >= 2:
                remove_cheese.append((x, y))

            print(remove_cheese, x, y)

        # for row in board:
        #     print(row)
        
        # print()
        # print(out_empty)
        
        # 없어지는 치즈들 없애주기
        for x, y in remove_cheese:
            board[y][x] = 0
            out_empty.add((x, y))
            total_cheese.remove((x, y))

        print(total_cheese, len(out_empty), answer)

        answer += 1

    print(answer)

    return

solution()





def firstSolu():

    '''
        다른 사람 풀이
        https://resilient-923.tistory.com/318


        나랑 좀 다른 방법으로 푸심 ㄷㄷ
        처음부터 BFS를 하면서
        공기칸을 기준으로 탐색을 진행함
        만약 치즈칸이 있으면 해당칸을 +1 해주는 방식으로 진행하면서
        치즈칸의 숫자가 3이되면 닿고 있는 공기칸이 2개 라는 뜻이 되어서
        삭제를 하는 방식

        풀이법이 신기했음 ㄷㄷㄷ


    '''

    n, m = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(n)]

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    def bfs():

        q = deque()
        q.append([0, 0])
        visited[0][0] = 1

        while q:
            x, y = q.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 0:
                    if graph[nx][ny] >= 1:
                        graph[nx][ny] += 1
                    else:
                        visited[nx][ny] = 1
                        q.append([nx, ny])
    
    time = 0
    while 1:

        visited = [[0] * m for _ in range(n)]

        bfs()

        flag = 0

        for i in range(n):
            for j in range(m):
                if graph[i][j] >= 3:
                    graph[i][j] = 0
                    flag = 1
                elif graph[i][j] == 2:
                    graph[i][j] = 1
        
        if flag == 1:
            time += 1
        
        else:
            break

    
    print(time)