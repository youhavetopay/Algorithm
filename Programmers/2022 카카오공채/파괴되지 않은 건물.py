def solution(board, skill):

    '''
        나의 풀이 (사실상 해설 보고 품..ㅠㅠ)
        공격과 회복을 했을때 남아있는 건물의 개수를 세는 문제

        나의 접근법
        처음엔 dict 자료형으로 중복된 skill 의 위치를 없애서 
        해줬지만 효율성 2개만 통과해서 실패..
        그래서 질문하기를 보니 누적합을 활용한 풀이라고 해서
        누적합활용해서 해보려고 했으나 1차원 배열에서는 했는데
        2차원 배열에서는 어떻게 해야할지 몰라서
        해설을 보고 품 ㅠㅠ

        2021 카카오 공채 문제 중 광고 삽입이라는 문제가 있었는데
        여기서 이런식으로 누적합을 사용해서 풀이를 한게 있었음..
        근데 너무 어려웠던건지 제대로 활용을 못함 ㅠㅠ
        너무 어렵다.,
    '''

    answer = 0

    # 누적합 기록용
    skill_board = [ [0] * (len(board[0]) + 1) for _ in range(len(board)+1)]

    for skil in skill:
        kind, y1, x1, y2, x2, degree = skil

        if kind == 1:
            degree *= -1

        # (x1, y1) ~ (x2, y2) 의 변화를 주고 싶으면
        # (x1, y1) = n, (x2+1, y1) = -n, (x1, y2+1) = -n, (x2+1, y2+1) = n 
        # 이렇게 해주면 됨
        skill_board[y1][x1] += degree
        skill_board[y1][x2+1] -= degree
        skill_board[y2+1][x1] -= degree
        skill_board[y2+1][x2+1] += degree

    # 가로로 누적합 구하기
    for y in range(len(skill_board)):
        now_sum = 0
        for x in range(len(skill_board[0])):
            skill_board[y][x] = now_sum + skill_board[y][x]
            now_sum = skill_board[y][x]

    # 세로로 누적합 구하기
    for x in range(len(skill_board[0])):
        now_sum = 0
        for y in range(len(skill_board)):
            skill_board[y][x] = now_sum + skill_board[y][x]
            now_sum = skill_board[y][x]

    for l in skill_board:
        print(l)

    # 누적합이랑 board랑 더해주기
    for y in range(len(board)):
        for x in range(len(board[0])):
            board[y][x] += skill_board[y][x]
            if board[y][x] >= 1:
                answer += 1
            

    return answer

print(solution([[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]], [[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]]))


def firstSolu(board, skill):

    '''
        다른 사람 풀이
        프로그래머스 다른 사람 풀이
        https://school.programmers.co.kr/learn/courses/30/lessons/92344/solution_groups?language=python3

        똑같은 풀이..
        근데 타입을 구별하는게 참 희한하게 하신듯? ㅋㅋ
    '''

    tboard = [[0] * (len(board[0] + 1)) for _ in range(len(board) + 1)]
    for typ, r1, c1, r2, c2, degree in skill:
        tboard[r1][c1] += (2*typ-3) * degree
        tboard[r2+1][c2+1] += (2*typ-3) * degree
        tboard[r2+1][c1] -= (2*typ-3) * degree
        tboard[r1][c2+1] -= (2*typ-3) * degree

    for i in range(1, len(tboard[0])):
        tboard[0][i] += tboard[0][i-1]
    for i in range(1, len(tboard)):
        tboard[i][0] += tboard[i-1][0]
    for x in range(1, len(tboard)):
        for y in range(1, len(tboard[0])):
            tboard[x][y] += tboard[x][y-1] + tboard[x-1][y] - tboard[x-1][y-1]
    
    ans = 0
    for x in range(len(board)):
        for y in range(len(board[0])):
            if board[x][y] + tboard[x][y] > 0 : ans += 1

    return ans