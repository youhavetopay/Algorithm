
'''
    백준 1167. 트리의 지름
    트리 연결 정보가 주어지면 임의의 두 점 사이의 최대 거리를 구하는 문제
'''

import sys
input = sys.stdin.readline

from collections import defaultdict
import heapq
sys.setrecursionlimit(1_000_000)

def solution():

    '''
        나의 풀이

        나의 접근법
        1967 문제랑 똑같은데 정점 개수만 더 많은 문제
        1967 은 1만개, 이거는 10만개

        그냥 똑같이 풀었더니 풀림 ㅋㅋㅋㅋㅋㅋㅋ
        1번 정점에서 다익스트라 한번 하고
        1번 정점에서 가장 먼 정점에서 다시 다익스트라해서
        그 결과값의 최대값을 하니 풀림...

        pypy3 이라서 풀렸나? 싶었는데
        python3 으로 해도 풀림 ㅋㅋㅋ
        오히려 python3 이 시간이랑 메모리를 더 적게 먹음 ㅋㅋㅋㅋㅋㅋㅋㅋ
        뭐지..ㅋㅋ
    '''

    V = int(input())
    # V = 5

    graph = defaultdict(list)

    # t = [
    #     [1, 3, 2, -1],
    #     [2, 4, 4, -1],
    #     [3, 1, 2, 4, 3, -1],
    #     [4, 2, 4, 3, 3, 5, 6, -1],
    #     [5, 4, 6, -1]
    # ]

    for _ in range(V):
        nums = list(map(int, input().split()))
        # nums = t[_]
        nums.pop()

        for i in range(1, len(nums)-1, 2):
            graph[nums[0]].append([nums[i], nums[i+1]])

    first_dist = dijkstra(graph, 1, V)
    max_idx = first_dist.index(max(first_dist))

    print(max(dijkstra(graph, max_idx, V)))

    return

def dijkstra(graph, start, n):

    dist = [float('inf')] * (n + 1)
    dist[0] = 0
    dist[start] = 0
    heap = [[0, start]]

    while heap:

        now_dist, now = heapq.heappop(heap)

        if dist[now] < now_dist:
            continue

        for next, cost in graph[now]:
            next_dist = now_dist + cost
            if dist[next] > next_dist:
                dist[next] = next_dist
                heapq.heappush(heap, [next_dist, next])

    return dist

# solution()


def my_second_solution():

    '''
        나의 두번째 풀이

        너무 문제를 쉽게 푼것 같아서 나 같은 사람이 있는지 
        질문 게시판을 좀 살펴봤는데 트리는 순한이 없기 때문에
        dp 를 통해서 더 빨리 구할 수 있다고 해서
        해보니까 풀림 ㅋㅋㅋ


        근데 pypy3 으로 하면 메모리 초과 뜸 ㅋㅋㅋ
        그리고 해보니까 dp 까지는 아니고 그냥 메모제이션 정도?
        저장 유무만 판단하고 나머지는 dfs 의 인자로 넣어줘서 DP 까지는 아닌듯...??
    '''

    V = int(input())
    # V = 5

    graph = defaultdict(list)

    # t = [
    #     [1, 3, 2, -1],
    #     [2, 4, 4, -1],
    #     [3, 1, 2, 4, 3, -1],
    #     [4, 2, 4, 3, 3, 5, 6, -1],
    #     [5, 4, 6, -1]
    # ]

    for _ in range(V):
        nums = list(map(int, input().split()))
        # nums = t[_]
        nums.pop()

        for i in range(1, len(nums)-1, 2):
            graph[nums[0]].append([nums[i], nums[i+1]])

    first_dist = dynamic_programming(graph, 1, V)
    max_idx = first_dist.index(max(first_dist))

    second_dist = dynamic_programming(graph, max_idx, V)
    print(max(second_dist))
    return

def dynamic_programming(graph, start, v):

    dp = [0] * (v + 1)
    dp[start] = -1


    def dfs(now_cost, now):

        for next, cost in graph[now]:
            if dp[next] == 0:
                dp[next] = now_cost + cost
                dfs(dp[next], next)

        return
    
    dfs(0, start)

    return dp

my_second_solution()


def firstSolu():

    '''
        다른 사람 풀이
        https://velog.io/@coding_egg/%EB%B0%B1%EC%A4%80-1991%EB%B2%88-%ED%8A%B8%EB%A6%AC%EC%9D%98-%EC%A7%80%EB%A6%84-python-%ED%8C%8C%EC%9D%B4%EC%8D%AC

        이 분은 BFS 를 두번 하는 방식으로 푸심
    '''

    from collections import deque
    read = sys.stdin.readline

    V = int(read())
    graph = [[] for _ in range(V + 1)]

    for _ in range(V):
        c = list(map(int, read().split()))
        for e in range(1, len(c) - 2, 2):
            graph[c[0]].append((c[e], c[e + 1]))
    
    def bfs(start):
        nonlocal V

        visist = [-1] * (V + 1)
        que = deque()
        que.append(start)
        visist[start] = 0
        _max = [0, 0]

        while que:
            t = que.popleft()

            for e, w in graph[t]:
                if visist[e] == -1:
                    visist[e] = visist[t] + w
                    que.append(e)

                    if _max[0] < visist[e]:
                        _max = visist[e], e

        return _max

    dis, node = bfs(1)
    dis, node = bfs(node)

    print(dis)

    return