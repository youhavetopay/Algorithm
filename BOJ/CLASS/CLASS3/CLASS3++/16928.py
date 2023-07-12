
'''
    백준 16928. ㅂ 과 사다리 게임

    1 ~ 100 까지 칸이 있는데
    주사위를 굴려서 1 ~ 6 칸 이동할 수 있고
    이동한 지점이 함정이나 사다리인 경우 거기로 이동하는데

    1에서 시작해서 100까지 도착하는데 최소로 굴려서 가는 횟수를 구하는 문제

    말이 어려워서 그렇지 방향있는 그래프에서 최단거리 찾기임 ㅋㅋ
'''

import sys
from collections import deque, defaultdict
input = sys.stdin.readline

ladder_count, trap_count = map(int, input().split())

ladders = []
traps = []

for _ in range(ladder_count):
    ladders.append(list(map(int, input().split())))

for _ in range(trap_count):
    traps.append(list(map(int, input().split())))

# ladder_count, trap_count = 4, 9

# ladders = [
#     [8, 52],
#     [6, 80],
#     [26, 42],
#     [2, 72]
# ]

# traps = [
#     [51, 19],
#     [39, 11],
#     [37, 29],
#     [81, 3],
#     [59, 5],
#     [79, 23],
#     [53, 7],
#     [43, 33],
#     [77, 21]
# ]

# ladder_count, trap_count = 3, 7

# ladders = [
#     [32, 62],
#     [42, 68],
#     [12, 98]
# ]

# traps = [
#     [95, 13],
#     [97, 25],
#     [93, 37],
#     [79, 27],
#     [75, 19],
#     [49, 47],
#     [67, 17]
# ]

# ladder_count, trap_count = 2, 1
# ladders = [
#     [2, 60],
#     [21, 99]
# ]

# traps = [
#     [61, 20]
# ]

def solution():

    '''
        나의 풀이

        나의 접근법
        처음엔 메모이제이션 해서 해당 지점에서 최소 횟수를 구해볼려고 했는데
        함정이랑 사다리의 순서에 따라 자꾸 값이 바껴서 어찌할지 모르고 있었는데
        
        알고리즘 유형을 보니까 BFS 라고 해서 다시 생각해보니

        방향 있는 그래프에서 최단 거리 검색하는 거였음 ㅡㅡ
        허무해..

        왜 이렇게 문제 접근을 잘 못하지..?
    '''
    
    graph = defaultdict(list)

    # 주사위를 굴려서 갈 수 있는곳 연결해주기
    for i in range(1, 101):
        graph[i] = []
        for j in range(i + 1, i + 7):
            if j >= 101:
                break
            graph[i].append(j)
    
    # 함정이거나 사다리면 별도로 처리해주기
    for start, end in traps:
        graph[start] = [end, False]
    
    for start, end in ladders:
        graph[start] = [end, False]

    visited = [False] * 101
    dist = [sys.maxsize] * 101
    queue = deque()
    visited[1] = True
    dist[1] = 0
    queue.append([1, 0])

    
    while queue:

        now, move_count = queue.popleft()

        next_move_count = move_count + 1

        # False 가 있으면 함정이나 사다리 이기 때문에
        # move_count 증가 안함 -> 바로 거기로 가기 때문에
        if False in graph[now]:
            next_move_count = move_count

        for next in graph[now]:
            if not str(next).isdigit():
                continue
            if visited[next] == False or dist[next] > next_move_count:
                
                visited[next] = True
                dist[next] = next_move_count
                queue.append([next, next_move_count])


    return dist[100]


print(solution())



def firstSolu():

    '''
        다른 사람 풀이
        https://data-flower.tistory.com/82

        나랑 똑같이 BFS 로 품

        특이한점은 나는 그래프를 전부 만들었는데
        이 분은 그래프를 만들지 않고 그냥 index로만 움직임

        그래서 그런지 조~~~금 더 빠른듯??
        그리고 함정이랑 사다리 체크를 먼저 해서 거기로 이동한 다음
        다음 이동할 거리를 체크해서 훨씬 깔끔한듯함 ㅋㅋ
    '''

    n, m = map(int, input().split())

    board = [0] * 101
    visited = [False] * 101

    ladder = dict()
    snake = dict()

    for _ in range(n):
        a, b = map(int, input().split())
        ladder[a] = b
    
    for _ in range(m):
        a, b = map(int, input().split())
        snake[a] = b
    
    q = deque([1])

    while q:
        x = q.popleft()

        if x == 100:
            print(board[x])
            break

        for dice in range(1, 7):
            next_place = x + dice

            if next_place <= 100 and not visited[next_place]:
                if next_place in ladder.keys():
                    next_place = ladder[next_place]

                if next_place in snake.keys():
                    next_place = snake[next_place]

                if not visited[next_place]:
                    visited[next_place] = True
                    board[next_place] = board[x] + 1
                    q.append(next_place)
