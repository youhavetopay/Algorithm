def solution(storey):

    '''
        나의 풀이
        절대값이 10의 거듭제곱으로만 이동할 수 있는
        엘리베이터가 있을때 현재 층에서 0층으로 가는데
        가장 적게 움직여서 가능 이동 수를 구하는 문제

        나의 접근법
        약간 그리디? 하게 풀었음
        층의 자리수 별로 체크해서
        6 이하라면 아래로 내려가는데
        5인 경우는 앞자리까지 체크하면 됨
        예외케이스 때문에 조금 힘들었음 -> 예외케이스는 힌트보고 암 ㅋㅋ

        문제 자체는 엄청 어려운건 아니라서
        그래도 노력하니까 금방 풀렸음
    '''

    answer = 0

    # 층을 각 자리수 별로 나눠놓기
    floors = list(map(int, str(storey)))
    # 맨앞에 0넣어주기 -> 계산하기 편하려고 ㅋㅋ
    floors = [0] + floors

    # 뒤에서부터 탐색
    for i in range(len(floors) -1, 0, -1):

        # 현재 수가 6보다 작으면
        # 아래층으로 내려가는게 더 빠름
        # 근데 5인 경우는 앞자리수까지 확인해 봐야 함 
        # ex) 75 같은 경우
        if floors[i] < 6:
            if (floors[i] == 5 and floors[i-1] >= 5):
                floors[i-1] += 1
                answer += 10 - floors[i]
            else:
                answer += floors[i]
        else:
            floors[i-1] += 1
            answer += 10 - floors[i]

    answer += floors[0]

    print(floors)

    return answer


print(solution(75))


def firstSolu(storey):

    '''
        다른 사람 풀이
        프로그래머스 다른 사람 풀이
        https://school.programmers.co.kr/learn/courses/30/lessons/148653/solution_groups?language=python3

        재귀로 위층에서 올라가는게 빠른지 아래층에서 내려가는게 빠른지 전부 검색 ㅋㅋㅋㅋ

    '''

    if storey < 10:
        return min(storey, 11 - storey)
    left = storey % 10
    return min(left + firstSolu(storey // 10), 10 - left + firstSolu(storey // 10 + 1))