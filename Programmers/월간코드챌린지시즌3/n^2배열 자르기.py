def solution(n, left, right):

    '''
        나의 풀이
        예시 에니메이션을 보고 만들어지는 
        리스트의 left부터 right까지의 부분 리스트를 만드는 문제

        나의 접근법
        일단 2차원 리스트가
        0번째 row -> 1, 2, 3, 4, ... , n
        1번째 row -> 2, 2, 3, 4, ... , n
        n-1 번째 row -> n-1, n-1, ... , n
        이런식으로 만들어져서

        left와 right가 몇번째 row의 index인지 계산하고
        left와 right번째의 row의 리스트를 만들어서 
        answer에 넣어주는 방식으로 품

        전체 2차원 리스트를 만드는 건 시간초과가 뜨더라도
        이렇게 부분 리스트를 만들어서 넣는건 시간초과 안뜨는 듯??
        아마 n = 1,000,000, left = 0, right = 1,000,000 ^ 2 - 1 이러는
        테스트 케이스는 없는듯?? ㅋㅋㅋㅋ
    '''

    answer = []

    # 각각 몇번째 row의 index인지 계산
    left_row, left_idx = left // n, left % n
    right_row, right_idx = right // n, right % n

    print(left_row, left_idx)
    print(right_row, right_idx)

    # left_row 번째 row 만들어주기
    left_rows = [left_row+1] * (left_row + 1)
    
    for i in range(left_rows[0]+1, n+1):
        left_rows.append(i)
        
    # left랑 right가 동일한 행인 경우
    if left_row == right_row:
        for i in range(left_idx, right_idx+1):
            answer.append(left_rows[i])
        
        return answer


    for i in range(left_idx, len(left_rows)):
        answer.append(left_rows[i])

    print(left_rows)
    
    # left_row < x < right_row 에 해당하는 row 만들어서 넣어주기
    for now_row in range(left_row + 1, right_row):
        now_rows = [now_row+1] * (now_row + 1)
        for i in range(now_rows[0]+1, n+1):
            now_rows.append(i)
        
        print(now_rows)

        for num in now_rows:
            answer.append(num)

    # right_row 번째 row 만들어서 넣어주기
    right_rows = [right_row+1] * (right_row + 1)
    
    for i in range(right_rows[0]+1, n+1):
        right_rows.append(i)
    
    print(right_rows)

    for i in range(0, right_idx+1):
        answer.append(right_rows[i])

    print(len(answer))
    return answer

print(solution(10, 0, 9))


def firstSolu(n, left, right):

    '''
        다른 사람 풀이
        프로그래머스 다른 사람 풀이
        https://school.programmers.co.kr/learn/courses/30/lessons/87390/solution_groups?language=python3

        해당 인덱스를 n으로 나눈 몫과 나머지를 통해
        n x n 리스트의 행과 열을 알 수 있는데
        이 중 더 높은것의 + 1이 해당 리스트의 값이라고 함...

        진짜 난 모르겠다 ㅋㅋ
    '''

    answer = []

    for i in range(left, right+1):
        answer.append(max(i // n, i % n) + 1)
    
    return answer