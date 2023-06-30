def solution(line):

    '''
        나의 풀이
        직선의 방정식들이 주어질때
        정수의 위치값을 가지는 교점들을
        최소의 크기??를 가지는 문자열 리스트로 표현하는 방법

        나의 접근법
        수학 문제이긴 하지만 다행히 두 직선간의 교점을 구하는 공식을 알려줘서
        교점은 쉽게 구했는데

        교점을 최소 크기의 문자열 리스트로 나타내는게 좀 힘들었음 ㅋㅋ
        별건 아닌데 웰케 힘들었지?? ㅋㅋㅋ

        내가 수학적 사고가 너무 떨어지는듯 ㅋㅋㅋㅋㅋㅋ
    '''

    answer = []

    cross_locs = set()

    # 직선 방정식의 교점 구하기
    for i in range(len(line)):

        a, b, e = line[i]
        for j in range(i+1, len(line)):
            c, d, f = line[j]

            # 이게 0이면 평행하거나 일치하는 것
            # 하지만 문제에서는 일치하는 직선은 주지 않는다고 함
            if ((a * d) - (b * c)) == 0:
                continue
            x = ((b * f) - (e * d)) / ((a * d) - (b * c))
            y = ((e * c) - (a * f)) / ((a * d) - (b * c))

            if x == int(x) and y == int(y):
                cross_locs.add((int(x), int(y)))
    
    print(cross_locs)

    # 좌표들의 최소값과 최대값 구하기
    min_x, max_x, = float('inf'), float('-inf')
    min_y, max_y = float('inf'), float('-inf')

    for x, y in cross_locs:
        if x < min_x:
            min_x = x
        if x > max_x:
            max_x = x

        if y < min_y:
            min_y = y
        if y > max_y:
            max_y = y
    
    print(min_x, max_x)
    print(min_y, max_y)

    # 구한 최소, 최대 값을 바탕으로 board 만들기
    board = [ ['.'] * (max_x - min_x + 1) for _ in range(max_y - min_y + 1)]

    # 알맞는 위치에 표시하기
    for x, y in cross_locs:
        # 이거 생각하는게 너무 어려웠음 ㅋㅋㅋ
        board[max_y - y][x - min_x] = '*'
    
    
    for t in board:
        answer.append(''.join(t))

    return answer

print(solution([[2, -1, 4], [-2, -1, 4], [0, -1, 1], [5, -8, -12], [5, 8, 12]]))


'''
    다른 사람 풀이
    프로그래머스 다른 사람 풀이
    https://school.programmers.co.kr/learn/courses/30/lessons/87377/solution_groups?language=python3

    한줄 ㅋㅋㅋㅋㅋㅋ
    대충 보면 로직은 얼추 비슷한듯??> ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ
'''
firstSolu = lambda line: (lambda rx, ry, s: ["".join("*" if (x, y) in s else "." for x in rx) for y in ry])(*((lambda i, j, s: (range(min(i), max(i) + 1), range(max(j), min(j) - 1, -1), s))(*(lambda s: ([v for v, _ in s], [v for _, v in s], s))(set((x // z, y // z) for x, y, z in [(b * f - e * d, e * c - a * f, a * d - b * c) for (a, b, e) in line for (c, d, f) in line] if z and not (x % z or y % z))))))