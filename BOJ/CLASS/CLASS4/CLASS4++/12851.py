
'''
    백준 12851. 숨바꼭질 2
    +1, -1, *2 3가지 방법으로 
    N 에서 K로 가는 최소 이동 횟수와 해당 경우의 수를 계산하는 문제
'''

import sys
input = sys.stdin.readline

from collections import deque

def solution():

    '''
        나의 풀이

        나의 접근법
        이전에 풀었던 숨바꼭질 문제와 다르게
        *2 하는데도 시간이 소모되도록 문제가 변경되었음
        그리고 경우의 수까지 계산해야 했기 떄문에 좀 고민좀 했음..

        처음엔 이동하는 그래프를 만들면서 최소 이동횟수를 구한 다음
        거기 까지 가는 경로를 계산하려고 했는데
        그리고 최단 경로 때문에 heap 을 사용하려고 했는데 
        어차피 이동하는데 사용되는 비용(시간)이 모두 1초라서 heap을 쓰는게 의미가 없는듯 해서
        deque로 바꿨고 생각해보니 굳이 그래프를 만들 필요도 없어서
        최단 비용을 기록하는 배열을 하나 만들어두고 같은 비용이 걸리는 곳이더라도 queue에 넣어주니 통과했음..!!

        이 문제는 어제 풀려다가 안풀고 다른 문제를 풀었는데
        그때 접근을 이상하게 한듯함 ㅋㅋㅋ

        이전에 11054 문제 풀려다고 못풀어서 이 문제를 봤는데 이 문제도 말려서
        좀 삽질좀 한듯 ㅋㅋㅋㅋㅋ

    '''

    N, K = map(int, input().split())
    # N, K = 5, 17

    min_times = [float('inf')] * 200_001
    min_times[N] = 0
    queue = deque([(0, N)])

    answer = 0

    while queue:
        now_time, now = queue.popleft()

        if now_time > min_times[K]:
            continue

        if now == K and now_time == min_times[K]:
            answer += 1
            continue

        a = now - 1
        b = now + 1
        c = now * 2

        for next in (a, b, c):

            if next < 0 or next > 150_000:
                continue

            if min_times[next] >= now_time + 1:
                min_times[next] = now_time + 1
                # heapq.heappush(heap, (now_time + 1, next))    
                queue.append((now_time + 1, next))
        
        # print(queue)
    print(min_times[K])
    print(answer)

    return

solution()


def firstSolu():

    '''
        다른 사람 풀이
        https://chul2-ing.tistory.com/71

        나랑 비슷한 풀이
        BFS 제한을 너 짧게 줘서 이게 좀더 효율적인듯??

        *2 해서 10만을 넘기고 -1 을 해주는 것 보다 *2 하기 전에 -1 해서 5만이 되었을때 *2 해주는게
        효율적이라서 10만은 안넘는다고 함
    '''

    n, k = map(int, input().split())

    queue = deque()
    queue.append(n)

    visited = [0] * 100001
    visited[n] = 0

    ans_count = 0
    ans_way = 0
    while queue:
        x = queue.popleft()
        count = visited[x]
        if x == k:
            ans_count = count
            ans_way += 1
            continue

        for nx in [x-1, x+1, 2*x]:
            if 0 <= nx < 100001:
                if visited[nx] == 0 or visited[nx] == visited[x] + 1:
                    queue.append(nx)
                    visited[nx] = count + 1
                    

    print(ans_count)
    print(ans_way)