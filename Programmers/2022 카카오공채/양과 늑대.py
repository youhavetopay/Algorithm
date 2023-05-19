import sys

class Node:
    def __init__(self, kind, index):
        self.index = index
        self.kind = kind
        self.child = []

    def set_p(self, p):
        self.p = p


def makeTree(info, edges):
    nodes = [None] * len(info)

    for edge in edges:
        p, c = edge
        
        if nodes[c] is None:
            nodes[c] = Node(info[c], c)

        child_node = nodes[c]
        
        if nodes[p]:
                nodes[p].child.append(child_node)
        else:
            nodes[p] = Node(info[p], p)
            nodes[p].child.append(child_node)

        child_node.set_p(nodes[p])

    return nodes


def gotoRoot(start, info, now_sheep, now_wolf):

    now = start
    wolf_count = 0

    while now.p:
        if info[now.index] == 1:
            info[now.index] = 0
            wolf_count += 1
            if now_sheep <= now_wolf + wolf_count:
                return sys.maxsize, info
        now = now.p
    
    return wolf_count, info

def solution(info, edges):

    '''
        나의 풀이
        이진트리에서 양과 늑대가 있을때
        최대한 얻을 수 있는 양의 마릿수를 계산하는 문제

        나의 접근법
        처음엔 DFS로 하나하나 탐색하려고 했으나
        단순 DFS로 하면 지역 최대값??에 빠질 수 있어서
        정답을 못찾음..
        그래서 양을 획득하는 경우의수로 계산 하려고 했는데
        경우의 수가 최대 16!.... 라서 백트래킹?? 방식으로 가지치기를 함

        양들의 위치를 리스트에 모아두고
        해당 위치에서 루트까지 가면서 늑대수를 체크함
        늑대수가 같아지지 않으면 해당 양은 획득 할 수 있으므로 
        해당 방식으로 품

        와... 많이 어려웠음 ㅋㅋㅋ
        어찌 저찌 풀었는데 좀 기분좋음 ㅋㅋㅋ
    '''

    # 양들의 위치를 기록
    sheep_index = []
    for i, kind in enumerate(info):
        if kind == 0:
            sheep_index.append(i)

    # 트리 만들어주기
    # 지금 보니 굳이 트리를 만들 필요는 없고
    # 그냥 내가 누구의 자식인지만 알면 될듯..ㅋㅋㅋ
    nodes = makeTree(info, edges)

    # 루트노드는 부모가 없으므로 None으로 해주기
    nodes[0].set_p(None)

    # 획득할 수 있는 양의 최대 마리수
    max_sheep_count = [0]

    def dfs(now_select, now_info, now_wolf):

        # 현재까지 선택한 양 -> 현재까지 획득한 양의 마리 수 
        if len(now_select) > max_sheep_count[0]:
            max_sheep_count[0] = len(now_select)
            

        for i in sheep_index:
            # 아직 해당 양을 선택하지 않았다면
            if i not in now_select:
                # 해당 양에서 root까지 가는데 있는 늑대 수와 트리정보 가져오기
                wolf_count, check_info = gotoRoot(nodes[i], now_info[:], len(now_select), now_wolf)
                # 해당 양을 가져올 수 있을 때
                if now_wolf + wolf_count < len(now_select) + 1:
                    # 다른 양 선택하기
                    dfs(now_select + [i], check_info, now_wolf + wolf_count)

                # 여기서 못가져오면 이 경우의 수는 못함
                # 다른 양 선택 하기
                else:
                    continue

    dfs([], info, 0)

    return max_sheep_count[0]

print(solution(	[0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0], [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [4, 8], [6, 9], [9, 10]]))


def firstSolu(info, edges):

    '''
        다른 사람 풀이
        https://velog.io/@thguss/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-L3-%EC%96%91%EA%B3%BC-%EB%8A%91%EB%8C%80-python

        너무 간단해서 허무함..ㅠ.....ㅠㅠㅠ

        그냥 방문 체크 하면서 계산하면 되는 거였음...
    '''

    visited = [0] * len(info)
    answer = []

    def dfs(sheep, wolf):
        if sheep > wolf:
            answer.append(sheep)
        else:
            return
        
        for p, c in edges:
            if visited[p] and not visited[c]:
                visited[c] = 1
                if info[c] == 0:
                    dfs(sheep + 1, wolf)
                else:
                    dfs(sheep, wolf + 1)
                visited[c] = 0


    visited[0] = 1
    dfs(1, 0)

    return max(answer)