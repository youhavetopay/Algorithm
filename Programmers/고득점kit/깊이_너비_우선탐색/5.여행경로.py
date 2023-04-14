import collections

def solution(tickets):

    '''
        나의 풀이 ㅋㅋㅋ

        오일러 트레일을 찾는 문제

        그냥 DFS로 모든 경로를 찾아서 정렬해서 찾는 방법으로 품 ㅋㅋㅋㅋㅋㅋ

        진짜 시작 공항을 안알려주고 공항 개수도 훨씬 더 많았다면 못풀었을 듯 ㅋㅋㅋ
        좀 어려웠음..ㅠㅠ
    '''

    graph = collections.defaultdict(list)

    # 티켓 정보 그래프로 나타내기
    for start, next in tickets:
        graph[start].append(next)

        # 도착하는 공항에서 다시 출발하는 티켓이 없을 수 있으니 만들어주기
        if next not in graph:
            graph[next] = []
    
    # 공항 목록 뽑아두기(정렬용)
    airports = list(sorted(graph.keys()))

    # 찾은 경로들
    find_routs = []

    # DFS
    def dfs(now, pre, now_graph):
        
        # 현재 남은 경로가 없을 때
        # 찾은 경로들에 넣어주기
        if ''.join(list(map(''.join, now_graph.values()))) == '':
            find_routs.append(pre[:])
            return
        
        # 티켓이 남았는데 현재 도착한 공항에서 아무데도 갈 수 없을 때
        # 잘못 온거라서 그냥 끝내기
        if len(now_graph[now]) == 0:
            return
        
        # 현재 공항에서 갈 수 있는 공항들로 탐색하기
        for i in range(len(now_graph[now])):
            temp = now_graph[now]
            pre.append(now_graph[now][i])
            now_graph[now] = now_graph[now][:i] + now_graph[now][i+1:]
            
            if len(now_graph[now]) == 0:
                del now_graph[now]

            dfs(pre[-1], pre, now_graph)

            pre.pop()
            now_graph[now] = temp

    
    routs_by_number = []

    dfs('ICN', ['ICN'], graph)

    # 찾은 경로들 중에서 알파벳 순으로 해야하기 때문에
    # 공항 목록의 index를 기준으로 숫자 만들어저 정렬해주기
    for idx, routs in enumerate(find_routs):

        number = ''
        for name in routs:
            number += str(airports.index(name))

        routs_by_number.append([number, idx])

    return find_routs[sorted(routs_by_number)[0][1]]

print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]))

def dfs(graph, N, key, footprint):

    # 종료조건 => 방문한 도시 수가 티켓 수 + 1일때
    if len(footprint) == N + 1:
        return footprint
    
    # 현재 도시에서 갈 수 있는 다음 도시 탐색
    # 종료조건에 만족하지 않고 현재도시에서 갈 수 있는데가 없다면 빈값 반환
    for idx, country in enumerate(graph[key]):

        # 나는 슬라이스 했는데
        # 생각해보니 pop, insert 해도 시간복잡도는 똑같을듯 ㅋㅋ
        graph[key].pop(idx)

        # 다음 도시를 목록에 넣어주기
        tmp = footprint[:]
        tmp.append(country)

        ret = dfs(graph, N, country, tmp)

        # 뺐던거 다시 넣어주기
        graph[key].insert(idx, country)

        # 결과값이 있을 때만 넘겨주기
        if ret:
            return ret


def firstSoul(tickets):

    '''
        다른 사람 풀이
        프로그래머스 다른 사람 풀이
        https://school.programmers.co.kr/learn/courses/30/lessons/43164/solution_groups?language=python3

        나랑 얼추 비슷하지만 훨씬 깔끔하고 빠름 ㅋㅋ
        티켓 수 + 1 이 정답의 길이라는게 조금 신기함 ㅋㅋㅋ 
        -> 당연한건가..?? ㅋㅋㅋ 그래프 다시 공부해야할듯 ㅋㅋ

    '''

    answer = []

    graph = collections.defaultdict(list)

    N = len(tickets)

    # 그래프 만들어주기
    # 알파벳 순서 때문에 정렬해주는듯??
    for ticket in tickets:
        graph[ticket[0]].append(ticket[1])
        graph[ticket[0]].sort()

    # DFS 시작
    answer = dfs(graph, N, 'ICN', ['ICN'])

    return answer