import collections

def solution(n, wires):

    '''
        나의 풀이
        그래프를 두개로 나누는데 노드 수의 차이가 최소가 되도록
        차이의 최소값을 찾는 문제

        연결 정보를 하나씩 빼면서
        BFS로 탐색을 해서 최소의 차이를 찾는 방식으로 품

        이것도 데이터 개수가 많지 않아서
        그냥 연결 정보를 하나씩 빼면서 확인하는 방식으로 품
    '''

    # 노드 수 차이 최대값
    answer = float('inf')

    # 그래프 연결정보
    graph = collections.defaultdict(list)

    for wire in wires:
        graph[wire[0]].append(wire[1])
        graph[wire[1]].append(wire[0])

    def bfs():

        # 방문 여부 체크
        visit = [False] * n
        queue = collections.deque()
        queue.append([1])
        visit[0] = True

        # BFS
        while queue:

            for node in queue.popleft():
                temp = []

                for next in graph[node]:
                    if not visit[next-1]:
                        temp.append(next)
                        visit[next-1] = True

                if temp:
                    queue.append(temp)

        # 아무 노드나 시작해서 BFS가 끝나면
        # 대충 그래프 하나를 다 탐색한거라서
        # 방문한 노드와 방문 안한 노드의 개수를 계산해서 반환
        return collections.Counter(visit)
    
    # 연결 정보 하나씩 빼면서 체크
    for wire in wires:

        graph[wire[0]].remove(wire[1])
        graph[wire[1]].remove(wire[0])

        # 그래프 탐색
        left, right = list(bfs().values())
        # 최소 값 구하기
        answer = min(answer, abs(left - right))

        graph[wire[0]].append(wire[1])
        graph[wire[1]].append(wire[0])

    return answer

print(solution(9, [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]))


def firstSoul(n, wires):

    '''
        다른 사람 풀이
        https://school.programmers.co.kr/learn/courses/30/lessons/86971/solution_groups?language=python3
        프로그래머스 다른 사람 풀이

        이게 뭐야.. ㅋㅋㅋㅋ
        뭔소린지 모르겠음 ㅋㅋ
        정말 파이써닉하게 푼듯 ㅋㅋ
    '''

    ans = n

    # 연결 정보 하나씩 뺀것들??
    for sub in (wires[i+1:] + wires[:i] for i in range(len(wires))):

        # 대충 set 연산을 통해서
        # 연결정보가 있다면 넣어주는 방식??
        s = set(sub[0])
        print(s)
        [s.update(v) for _ in sub for v in sub if set(v) & s]
        print(s)
        print()

        # 최소 차이를 구하는데
        # 왜 len(s) * 2하는거지?? ㅋㅋ
        ans = min(ans, abs(2 * len(s) - n))
    
    return ans

print(firstSoul(9, [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]))