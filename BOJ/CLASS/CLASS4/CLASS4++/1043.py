
'''
    백준 1043. 거짓말
    진실을 아는 사람이 있을 때
    내가 거짓말쟁이로 들통나지 않는 최대 거짓말 횟수를 구하는 문제
'''

import sys
input = sys.stdin.readline

from collections import defaultdict, deque

def solution():

    '''
        나의 풀이

        나의 접근법
        처음엔 문제 제대로 안읽고 단순하게
        해당 파티에서 진실을 알고 있는 사람이 없으면 거짓말을 하는 방식으로 했는데
        예제 테스트케이스랑 정답이 다르길래 뭐지 했더니
        내가 진실을 말한 파티에서 참석한 사람은 진실을 알고 있는 사람에게 추가되고
        파티 순서는 상관이 없어야 한다는걸 알았음.. ㅋㅋㅋㅋ

        그래서 파티 참여자 정보를 그래프로 나타내고
        진실을 알고 있는 사람을 기준으로 BFS를 해주면서 연결된 사람을 체크함 -> 진실을 알고 있는 사람 업데이트

        그렇게 구해진 사람들을 바탕으로 파티 참석 정보를 체크하는 방식으로 하니까 풀림 ㅎㅎ

        그래프 탐색 응용 문제인데 그래프로 풀 수 있는 걸 너무 늦게 알아차린듯 함.. ㅋㅋㅋ
    '''

    N, M = map(int, input().split())

    true_nums = list(map(int, input().split()))
    true_nums.pop(0)
    true_nums = set(true_nums)

    # 그래프 만들기
    graph = defaultdict(set)
    partys = []
    for _ in range(M):
        party = list(map(int, input().split()))

        for i in range(1, len(party)):
            a = party[i]
            for j in range(i+1, len(party)):
                b = party[j]
                graph[a].add(b)
                graph[b].add(a)
        
        party.pop(0)
        partys.append(party)
                
    visited = set()
    temp = list(true_nums)
    if temp == []:
        print(M)
        return


    queue = deque(temp)
    visited.add(temp[0])

    # BFS
    while queue:

        now = queue.popleft()

        for next in graph[now]:
            if next not in visited:
                queue.append(next)
                true_nums.add(next)
                visited.add(next)
    
    # 거짓말 가능한지 체크하기
    answer = 0
    for party in partys:
        for t_num in true_nums:
            if t_num in party:
                break
        else:
            answer += 1

    print(answer)
    return

solution()



def firstSolu():

    '''
        다른 사람 풀이
        https://ku-hug.tistory.com/148

        교집합과 합집합을 이용해서 품 ㄷㄷㄷ

        파티 참가자와 진실을 알고 있는 사람들의 교집합이 있으면
        진실을 알고 있는 사람을 업데이트 해줌 -> 합집합

        이게 훨~~~~~~~~~~~~~~~씬 깔끔한듯 ㅋㅋㅋㅋㅋ
    '''

    n, m = map(int, input().split())
    knowList = set(input().split()[1:])
    parties = []

    for _ in range(m):
        parties.append(set(input().split()[1:]))
    
    for _ in range(m):
        for party in parties:
            if party & knowList:
                knowList = knowList.union(party)

    cnt = 0

    for party in parties:
        if party & knowList:
            continue
        cnt += 1
    
    print(cnt)