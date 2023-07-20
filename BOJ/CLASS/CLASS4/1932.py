
'''
    백준 1932. 정수 삼각형
    삼각형 형태로 2차원 배열이 주어지면
    루트에서 맨 밑층까지 자식 중 하나의 숫자를 더해서 최대값을 찾는 문제
'''

import sys
input = sys.stdin.readline

n = int(input())
triangle = [ list(map(int, input().split())) for _ in range(n)]

def solution(n, triangle):

    '''
        나의 풀이
        
        나의 접근법
        처음엔 아무 생각없이 BFS로 했더니
        메모리초과 뜨길래 뭐지 싶었음 ㅋㅋ

        그래서 다시 확인해보니 최대 노드 갯수가 49,995,000 ㅋㅋㅋㅋ
        그래서 DFS 다시 확인해보니 시간초과가 떴었음 ㅋㅋㅋ

        곰곰히 생각해봤는데
        분할정복도 아니라서 완전탐색은 아니라고 결론이 나왔음
        그럼 DP 인가? 해서 봤더니 맞았음 ㅋㅋㅋ
        뭔가 문제가 1149. RGB거리 문제랑 비슷한것 같아서 DP 로 해봤는데 맞았음 ㅋㅋㅋ

        맨 왼쪽끝 과 오른쪽 끝은 부모가 1개라서 그거 넣어주면 되고
        나머지 중간들은 두 부모의 수 중에서 큰 수를 더해주면 됨

        약간 완전탐색 안되면 DP 로 해보는 것도 나쁘진 않을듯??
    '''

    for y in range(n-1):
        
        for x in range(len(triangle[y+1])):
            if x == 0:
                triangle[y+1][x] += triangle[y][x]
            elif x == len(triangle[y+1]) - 1:
                triangle[y+1][x] += triangle[y][x-1]
            else:
                triangle[y+1][x] += max(triangle[y][x], triangle[y][x-1])

    return max(triangle[-1])

print(solution(n, triangle))


def firstSolu():

    '''
        다른 사람 풀이
        https://velog.io/@bye9/%EB%B0%B1%EC%A4%80%ED%8C%8C%EC%9D%B4%EC%8D%AC-1932-%EC%A0%95%EC%88%98-%EC%82%BC%EA%B0%81%ED%98%95

        나랑 똑같은 풀이 ㅋㅋㅋ
    '''

    n = int(input())
    d = []
    for i in range(n):
        d.append(list(map(int, input().split())))

    for i in range(1, n):
        for j in range(len(d[i])):
            if j == 0:
                d[i][j] = d[i][j] + d[i-1][j]
            elif j == len(d[i]) - 1:
                d[i][j] = d[i][j] + d[i-1][j-1]
            else:
                d[i][j] = max(d[i-1][j], d[i-1][j-1]) + d[i][j]
    
    print(max(d[n-1]))