import collections

def solution(n, path, order):

    '''
        나의 풀이(해석 보고 품..ㅠㅠ)
        방문 순서가 정해진 그래프를 모두 탐색할 수 있는지 체크하는 문제

        나의 접근법(풀이법을 보고 해서 혼자서 푼것 아님..ㅋㅋ)
        먼저 그래프를 만들고 BFS를 함
        그리고 아직 잠긴 노드에 방문하려고 하면 체크해 뒀다가
        해제 할 수 있으면 그때 queue에 넣어주는 방식으로 품

        못 방문한 동굴을 체크해뒀다가 해제되면 그때 queue에 넣어주는게
        키 포인트라고 함
        
        그래도 나름 혼자서 하다가 마지막 효율성에서 자꾸 시간초과떠서
        엄청 아쉬운 문제였음
    '''

    graph = collections.defaultdict(list)
    unlock_caves = {}
    lock_caves = set()

    # 그래프 만들어주기
    for start, end in path:
        graph[start].append(end)
        graph[end].append(start)

    # 잠긴 동굴이랑 해제하는 동굴 기록하기
    # 0은 무조건 첫번째 방문해야 하므로 해제 동굴의 의미가 없음
    for first, last in order:
        if first != 0:
            unlock_caves[first] = last
            lock_caves.add(last)

    # 만약에 0번 동굴이 잠긴 동굴이라면 시작을 못함
    if 0 in lock_caves:
        return False
    
    
    visit = [False] * n
    queue = collections.deque([0])
    visit[0] = True

    not_search_caves = set()

    # BFS 시작
    while queue:
        now_cave = queue.popleft()
        
        for next_cave in graph[now_cave]:
            if visit[next_cave] == False:
                
                # 해당 동굴이 잠긴 동굴이면 방문 못한 동굴 목록에 넣어주기
                if next_cave in lock_caves:
                    not_search_caves.add(next_cave)
                    continue
                
                # 해당 동굴이 해제하는 동굴일때
                if next_cave in unlock_caves:

                    # 잠긴 동굴 해제 해주기
                    lock_cave = unlock_caves[next_cave]
                    lock_caves.remove(lock_cave)

                    # 잠긴 동굴이 방문 못한 동굴이라면 queue에 넣어주기
                    if lock_cave in not_search_caves:
                        visit[lock_cave] = True
                        queue.append(lock_cave)
                        not_search_caves.remove(lock_cave)

                    del unlock_caves[next_cave]
                    
                visit[next_cave] = True
                queue.append(next_cave)
    
    # BFS가 끝났는데 방문 못한 동굴이 있는지 체크
    return all(visit)

print(solution(9, [[0, 1], [0, 3], [0, 7], [8, 1], [3, 6], [1, 2], [4, 7], [7, 5]], [[8, 5], [6, 7], [4, 1]]))


def firstSolu(n, path, order):
    
    '''
        다른 사람 풀이
        프로그래머스 다른 사람 풀이

        나랑 비슷한 풀이인데
        훨씬 깔끔한듯?? ㅋㅋㅋ
        근데 변수 이름은 queue인데 하는 행동은 stack인듯??? ㅋㅋㅋㅋㅋ
        아마 DFS로 하신듯 함
    '''

    # 그래프 만들기
    graph = [[] for i in range(n)]
    while path:
        src, dest = path.pop()
        graph[src].append(dest)
        graph[dest].append(src)
    
    destination = set()
    src2dest = [0] * n

    # 잠긴 동굴이랑 해제 동굴 기록
    for src, dest in order:
        destination.add(dest)
        src2dest[src] = dest
    
    queue = [0]
    visited = [False] * n

    # 시작
    while queue:

        # DFS 맞는듯 ㅋㅋㅋ
        node = queue.pop()
        visited[node] = True
        dest = src2dest[node]

        # 현재 동굴이 해제하는 동굴일 때
        if dest:

            # 잠긴 동굴을 해제시키고 
            # 해당 동굴을 체크 했었다면(continue) 
            # 해당 동굴이랑 연결된 동굴 중 방문 안한 동굴을 추가해주기
            destination.remove(dest)
            if visited[dest]:
                queue.extend([adj for adj in graph[dest] if not visited[adj]])
        elif node in destination:
            continue
        
        # 다음 동굴들 넣어주기
        queue.extend([adj for adj in graph[node] if not visited[adj]])
    
    return not destination