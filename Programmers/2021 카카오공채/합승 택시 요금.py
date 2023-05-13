from collections import defaultdict, deque
import sys

MAX_VALUE = sys.maxsize

def bfs(start, n, graph):

    total_costs = [MAX_VALUE] * n

    total_costs[start] = 0

    q = deque()
    q.append([start, 0])

    while q:
        now, now_cost = q.popleft()

        for next, cost in graph[now]:
            next_cost = now_cost + cost
            if total_costs[next] >= next_cost:
                total_costs[next] = next_cost
                q.append([next, next_cost])
    
    return total_costs


def solution(n, s, a, b, fares):

    '''
        나의 풀이
        출발지점에서 서로 다른 두 지점을 갈때
        공통된 비용과 각각의 위치까지의 비용을 더한 값을 구하는 문제?? ㅋㅋㅋ
        대충 택시 합승요금 + 해당 위치에서 목적지까지의 각각의 비용 합?? ㅋㅋㅋ

        나의 접근법
        BFS로 출발지에서 다른 곳까지의 최소 비용을 구하고
        나머지 위치에서 다시 BFS로 다른 곳 까지의 최소비용을 각각 구한 후
        계산하는 방식으로 품

        레벨 3인데도 불구하고 힌트도 안보고 엄청 빨리품
        효율성은 모르겠지만 어찌됐든 통과는 했으니.. ㅋㅋㅋㅋ
        아마 정점이 200개 이하라서 통과한듯..?? ㅋㅋㅋㅋ
    '''

    answer = MAX_VALUE

    # 1번 부터 있어서 0번부터 가능하도록 1씩 빼주기
    s -= 1
    a -= 1
    b -= 1

    # 그래프 만들기
    graph = defaultdict(list)
    for start, end, cost in fares:
        start -= 1
        end -= 1
        graph[start].append([end, cost])
        graph[end].append([start, cost])

    # BFS로 최소 비용구하기
    start_costs = bfs(s, n, graph)

    # 기본값 
    # 시작 점에서 각각의 목적지까지의 비용
    answer = start_costs[a] + start_costs[b]

    # 다른 곳까지 합승 한 경우 계산하기
    for i in range(n):
        if i == s:
            continue
        # 해당 지점에서 BFS하기
        new_costs = bfs(i, n, graph)
        # 기존에 시작점에서 계산한 비용과 해당 지점에서의 최소비용 더해주기
        answer = min(answer, new_costs[a] + new_costs[b] + start_costs[i])


    return answer

print(solution(6, 4, 6, 2, [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]))


def firstSolu(n, s, a, b, fares):

    '''
        다른 사람 풀이
        프로그래머스 다른 사람 풀이

        플로이드 워셜 알고리즘이라고 함..ㄷㄷㄷ
        플로이드 워셜은 다익스트라와 다르게
        모든 노드간의 최단 거리를 계산하는 알고리즘이고 O(v^3) 알고리즘이라서
        정점 수가 작으면 간단하게 3중 반복문으로 해결할 수 있다고 함

        실행시켜보니 위에 내 풀이는 최대 8000ms까지 나오는데
        이 풀이는 최대 2000ms로 굉장히 안정적인 실행 속도가 나옴 ㄷㄷ
    '''

    d = [ [20000001 for _ in range(n)] for _ in range(n)]

    for x in range(n):
        d[x][x] = 0
    
    for x, y, c in fares:
        d[x-1][y-1] = c
        d[y-1][x-1] = c

    for i in range(n):
        for j in range(n):
            for k in range(n):
                if d[j][k] > d[j][i] + d[i][k]:
                    d[j][k] = d[j][i] + d[i][k]
    
    minv = 40000002
    for i in range(n):
        minv = min(minv, d[s-1][i] + d[i][a-1] + d[i][b-1])
    
    return minv