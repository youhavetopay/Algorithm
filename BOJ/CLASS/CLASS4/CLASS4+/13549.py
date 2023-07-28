
'''
    백준 13549. 숨바꼭질 3
    일정 거리를 이동할 수 있을때
    목표지점까지 가는 최단 시간을 구하는 문제
'''

import sys
sys.setrecursionlimit(200_000)
input = sys.stdin.readline

N, K = map(int, input().split())


def solution(n, k):

    '''
        나의 풀이

        나의 접근법
        처음에 완전탐색으로 했다가 당연히 시간초과로 실패함
        그래서 백트래킹이라고 생각해서
        좀 고민좀 하다가 반대로 목적지에서 출발지 까지 이동하면
        약간 탐욕스럽게 할 수 있을 것 같아서 시도를 해보고
        중복 탐색을 막으려고 dict에 현재 까지 걸린 시간을 기록해둠
        그랬는데 자꾸 틀리길래 반례 좀 찾아봤는데

        나는 현재 위치가 짝수이고 현재 위치가 목표지점보다 클때만
        나누기 2를 하는 방식을 했는데
        현재 위치가 6이고 목표지점이 5일 때는 나누기를 해버려서 최단 시간을 못찾았음
        그래서 나누기 2를 하는 조건을 추가해줬더니 통과함 ㅎㅎ

        근데 질문개시판에 사람들이 전부 다 다익스트라, 너비우선 이런걸 해뒀길래
        오기로 계속 풀었음 ㅋㅋ

        근데 나도 사실상 다익스트라랑 비슷해서 큰?? 차이는 없을듯??
    '''

    # 현재 위치가 목적지랑 같을 때
    if k == n:
        return 0
    
    # 현재 위치가 목표위치보다 높을때
    # 뒤로가는게 -1 밖에 없음
    if k < n:
        return n-k
    
    # 현재 위치까지 걸리는 최소 시간
    dp = {n:abs(n-k)}

    def dfs(now_loc, now_time, road):

        # 현재 위치가 마이너스로 가면 안됨
        if now_loc < 0:
            return

        # 이미 방문한 곳일 때
        if now_loc in dp:
            
            # 현재까지 걸린 시간이 같거나 크면 끝내기
            if dp[now_loc] <= now_time:
                return
            else:
                # 최소 값 갱신
                dp[now_loc] = now_time
        else:
            # 방문 기록
            dp[now_loc] = now_time

        # 목표지점에 도착했다면 끝내기
        if now_loc == n:
            print(road)
            return

        # 현재 위치가 짝수이고 목표지점보다 높고
        # 현재 위치에서 1칸씩 이동하는 것보다 나누기 2 해서 1칸씩 이동하는게 더 짧을때
        # 이러한 조건을 만족하면 무조건 나누기 2 하는게 이득임
        if now_loc % 2 == 0 and now_loc > n and abs(now_loc - n) > abs(now_loc // 2 - n):
            dfs(now_loc // 2, now_time, road + [now_loc // 2])
        else:
            # 나머지때는 그냥 1칸씩 이동하기
            dfs(now_loc + 1, now_time + 1, road + [now_loc + 1])
            dfs(now_loc - 1, now_time + 1, road + [now_loc - 1])

        
    dfs(k, 0, [k])
    print(dp)

    return dp[n]

print(solution(N, K))

from collections import deque
def firstSolu():

    '''
        다른 사람 풀이
        https://jshong1125.tistory.com/29

        BFS 로 하심
        대신 곱하기 하는게 왠만하면 이득이라서 큐 앞에 넣어줌

        생각보다 엄청 간단해서 신기함 ㅋㅋ
    '''

    n, k = map(int, input().split())
    q = deque()
    q.append(n)
    visited = [-1 for _ in range(100_001)] # 방문 여부 체크 및 시간 기록
    visited[n] = 0

    while q:
        s = q.popleft()

        if s == k:
            print(visited[s])
            break
        
        # 각자 방문하지 않았고 해당 범위를 만족하면
        # 현재 시간 기록하고 큐에 넣어줌

        if 0 <= s-1 < 100_001 and visited[s-1] == -1:
            visited[s-1] = visited[s] + 1
            q.append(s-1)
        
        if 0 < s * 2 < 100_001 and visited[s*2] == -1:
            visited[s*2] = visited[s]
            q.appendleft(s*2) # 곱하기 2 하는게 우선
        
        if 0 <= s+1 < 100_001 and visited[s+1] == -1:
            visited[s+1] = visited[s] + 1
            q.append(s+1)