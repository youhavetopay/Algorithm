
'''
    백준 1987. 알파벳
    알파벳으로 이뤄진 보드가 있을때 중복되지 않는 칸에 방문하는 
    최대의 이동 수를 구하는 문제
'''

import sys
input = sys.stdin.readline

def solution():

    '''
        나의 풀이(100% 내가 푼건 아님 ㅋㅋ)

        나의 접근법

        처음엔 BFS로 했는데 이전에 방문한 알파벳을 기억하고 있어야 해서 그런지
        메모리 초과가 떴음..

        그래서 DFS로 바꾸고 방문 기록을 set으로 했는데
        시간초과가 떴음...

        그래서 어차피 알파벳만 나오니까 최대 깊이 값을 26으로 제한하고
        dict 자료형으로 알파벳에 대한 체크를 해줌
        그랬는데도 시간초과가 뜨길래

        결국 질문하기 게시판을 보니까
        방문여부는 배열로 하고 direction 을 배열이 아닌 튜플로 바꿔주니 통과함

        개인적으로 이렇게 시간제한 빡빡한 문제는 별로....
    '''

    R, C = map(int, input().split())

    board = [input().rstrip() for _ in range(R)]

    direction = ((1, 0), (-1, 0), (0, 1), (0, -1))
    
    answer = 0

    visited = [0] * 26

    def dfs(x, y, move_count):

        nonlocal answer, R, C

        answer = max(answer, move_count)

        if move_count == 26:
            return

        for dx, dy in direction:
            nx, ny = x + dx, y + dy

            

            if 0 <= nx < C and 0 <= ny < R:
                
                n_word_i = ord(board[ny][nx]) - 65

                if visited[n_word_i] == 0:
                    visited[n_word_i] = 1
                    dfs(nx, ny, move_count + 1)
                    visited[n_word_i] = 0

    visited[ord(board[0][0]) - 65] = 1
    dfs(0, 0, 1)

    print(answer)

    return

solution()


def firstSolu():

    '''
        다른 사람 풀이
        https://sorryhyeon.tistory.com/34

        배열에서 값 가져올때는 zip 해서 가져오는 것 보단
        index로 접근하는게 더 빠른듯.....
    '''

    r, c = map(int, input().split())
    maps = []
    for _ in range(r):
        maps.append(list(input()))
    ans = 0
    alphas = set()
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    def dfs(x, y, count):
        nonlocal ans
        ans = max(ans, count)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < r and 0 <= ny < c and not maps[nx][ny] in alphas:
                alphas.add(maps[nx][ny])
                dfs(nx, ny, count+1)
                alphas.remove(maps[nx][ny])
    alphas.add(maps[0][0])
    dfs(0, 0, 1)
    print(ans)