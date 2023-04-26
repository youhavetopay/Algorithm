def solution(board, moves):

    '''
        나의 풀이
        인형뽑기해서 스택에 쌓는데
        같은거 연속으로 있으면 없애고 없앤 횟수를 계산하는 문제

        나의 접근법
        그냥 게임 로직 그대로 구현함..

        예전에 풀었던 문제라서
        그냥 저냥 풀었는데
        처음에 집게 이동까지 내가 구현해야하는 줄 알고 식겁함 ㅋㅋㅋ

        예전에는 pop을 안쓰고 del stack[-1] 했었음 ㅋㅋㅋㅋ
    '''

    answer = 0

    stack = []
    board_height = len(board)

    for x in moves:

        # 가로 위치 -1 해주기
        x -= 1

        # 0이 아닐때까지 집게 내리기
        now_y = 0
        while now_y < board_height and board[now_y][x] == 0:
            now_y += 1
        
        # 만약 해당 라인이 비었으면 다음 라인으로 넘어가기
        if now_y >= board_height:
            continue
        
        # 스택에 담아주고 같으면 횟수 카운팅 해주기
        if stack and stack[-1] == board[now_y][x]:
            stack.pop()
            answer += 2
        else:
            stack.append(board[now_y][x])

        # 집어갔으니까 해당 칸 비워주기
        board[now_y][x] = 0

    return answer

print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4]))


def firstSolu(board, moves):

    '''
        다른 사람 풀이
        프로그래머스 다른 사람 풀이
        
        나랑 비슷하게 풀었는데
        코드가 훨씬 깔끔한듯..??? ㅋㅋㅋ
    '''

    stacklist = []
    answer = 0

    for i in moves:
        for j in range(len(board)):
            if board[j][i-1] != 0:
                stacklist.append(board[j][i-1])
                board[j][i-1] = 0

                if len(stacklist) > 1:
                    if stacklist[-1] == stacklist[-2]:
                        stacklist.pop(-1)
                        stacklist.pop(-1)
                        answer += 2
                
                break

    return answer


def secondSolu(board, moves):

    '''
        다른 사람 풀이 2
        프로그래머스 다른 사람 풀이

        풀이가 특이해서 가져옴 ㅋㅋ
        참 파이써닉 함 ㅋㅋㅋ
    '''

    # 행과 열을 바꿈 -> 행은 열, 열은 행으로
    # 그리고 필터걸어서 0이 아닌것만 가져옴
    cols = list(map(lambda x: list(filter(lambda y: y > 0, x)), zip(*board)))
    print(cols)
    a, s = 0, [0]

    # 그 다음은 동일함
    for m in moves:
        if len(cols[m - 1]) > 0:
            # := 변수 만들어주는 거
            d = cols[m - 1].pop(0)
            l = s.pop()
            if d == l:
                a += 2
            else:
                s.extend([l, d])

    return a

print(secondSolu([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4]))