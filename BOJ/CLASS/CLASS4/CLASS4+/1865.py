
'''
    백준 1865. 웜홀
    출발해서 다시 돌아오는 비용이 음수가 되는 경로가 있는지 없는지
    체크하는 문제
'''

import sys
input = sys.stdin.readline

from collections import defaultdict

def bellman():

    N, M, W = map(int, input().split())

    graph = defaultdict(list)

    for _ in range(M):
        start, end, time = map(int, input().split())
        start -= 1
        end -= 1

        graph[start].append([end, time])
        graph[end].append([start, time])
    
    for _ in range(W):
        start, end, time = map(int, input().split())
        start -= 1
        end -= 1
        time = -time

        graph[start].append([end, time])


    dists = [sys.maxsize] * N
    
    for i in range(N):
        for start in range(N):
            for next, time in graph[start]:
                if dists[next] > dists[start] + time:
                    dists[next] = dists[start] + time
                    if i == N-1:
                        print('YES')
                        return
    
    print('NO')
    return


def solution():

    '''
        나의 풀이(못품..)

        나의 접근법
        처음엔 플로이드워셜 쓰면 될줄 알았는데
        정점의 수가 500이고 심지어 테스트케이스 개수고 최대 5개라서
        하니까 시간초과가 떴음..

        그러면 벨만포드 밖에 없는 것 같아서
        벨만포드 공부해서 

        웜홀이 있는 곳에서 벨만포드를 하고
        음수 사이클? 이 존재하면 YES를 출력하도록 했는데

        이것도 시간초과가 나왔음..ㅋㅋ

        그래서 결국 정답을 봤는데
        일반적인 벨만포드와는 달리 시작점이 중요하지 않기 때문에
        계산된 노드? 인지 체크하는 부분을 빼주고

        한번만 벨만포드를 해주면 풀린다고 함..

        솔직히 벨만포드가 직관적으로 이해가 잘 안됨...ㅠㅠ

        열심히 해보자..

    '''

    T = int(input())

    for _ in range(T):
        bellman()
        

solution()

def bf(n, edges, dist):
    for i in range(n):
        for j in range(len(edges)):
            cur, next, cost = edges[j]
            if dist[next] > dist[cur] + cost:
                dist[next] = dist[cur] + cost
                if i == n - 1:
                    return True
                
    return False

def firstSolu():
    
    '''
        다른 사람 풀이
        https://ku-hug.tistory.com/127

        똑같이 벨만포드로 하심

    '''

    TC = int(input())

    for _ in range(TC):
        n, m, w = map(int, input().split())
        edges = []
        dist = [1e9] * (n + 1)

        for i in range(m + w):
            s, e, t = map(int, input().split())

            if i > m:
                t = -t
            else:
                edges.append((e, s, t))
            edges.append((s, e, t))
    
    if bf(n, edges, dist):
        print("YES")
    else:
        print('NO')