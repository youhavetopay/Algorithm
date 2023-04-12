import collections

def solution(n, computers):

    '''
        나의 풀이
        그래프 개수 찾는 문제

        BFS로 품

        깊이/너비 우선 탐색 기본문제라서 어렵지 않았음
        대신 index를 queue에 넣어야 하는데 자꾸 연결 값을 넣어서
        헷갈렸음 ㅋㅋㅋㅋ
    '''

    answer = 0

    visit = [False] * n

    queue = collections.deque()

    # 모두 방문할때 까지
    while not all(visit):

        # 아직 방문 안한 노드 있을 때 넣어주기
        for idx, flag in enumerate(visit):
            if flag == False:
                queue.append([idx])
                visit[idx] = True
                break
    
        # 큐를 비울때까지 -> 한 그래프를 다 탐색할때까지
        # BFS 시작
        while queue:
            print('start', queue, visit)

            now_nodes = queue.popleft()

            next_nodes = []
            for node in now_nodes:
                for idx, value in enumerate(computers[node]):
                    if value == 1 and node != idx and visit[idx] == False:
                        next_nodes.append(idx)
                        visit[idx] = True
            
            if next_nodes:
                queue.append(next_nodes)
            
            print('end', queue, visit)

        # 한번의 BFS가 끝나면 그래프 개수 올려주기
        answer += 1
        print(visit)
        print()

    return answer

print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))


def firstSoul(n, computers):

    '''
        다른 사람 풀이
        프로그래머스 다른 사람 풀이
        https://school.programmers.co.kr/learn/courses/30/lessons/43162/solution_groups?language=python3

        DFS 풀이

        개인적이지만
        그래프 탐색할때는 BFS가 좀더 익숙해서..??? 보통 BFS로 하는 편인데
        DFS가 재귀?? 함수의 기본 같은 느낌이라서
        좀 익숙해질 필요가 있을 듯 함
    '''

    answer = 0
    visited = [0 for i in range(n)]

    def dfs(computers, visited, start):

        stack = [start]
        while stack:
            j = stack.pop()
            if visited[j] == 0:
                visited[j] = 1
            
            for i in range(0, len(computers)):
                if computers[j][i] == 1 and visited[i] == 0:
                    stack.append(i)
    
    i = 0

    while 0 in visited:
        if visited[i] == 0:
            dfs(computers, visited, i)
            answer += 1
        
        i += 1

    return answer


def secondSoul(n, computers):

    '''
        두번째 다른 사람 풀이
        프로그래머스 다른 사람 풀이
        https://school.programmers.co.kr/learn/courses/30/lessons/43162/solution_groups?language=python3

        3중 for 문으로 푼게 인상적이라서 들고 옴 ㅋㅋ
        대충 같은 네트워크에 있는 노드들을 같은 숫자로 만들어주는 것이라고 하는데
        이해 안감 ㅋㅋㅋㅋ
        플로이드-워셜 알고리즘을 활용한 풀이라고 하는데 자세히 모르겠음 ㅋㅋㅋㅋㅋ
    '''

    temp = []
    for i in range(n):
        temp.append(i)
    
    for i in range(n):
        for j in range(n):
            if computers[i][j]:
                for k in range(n):
                    if temp[k] == temp[i]:
                        temp[k] = temp[j]
    
    return len(set(temp))
