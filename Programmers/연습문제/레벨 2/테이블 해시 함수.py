def solution(data, col, row_begin, row_end):

    '''
        나의 풀이
        2차원 리스트가 주어질때
        일정한 규칙에 따라 정렬하고
        정렬된 리스트의 일정구간의 연산 값을 구하는 문제

        나의 접근법
        그냥 구현하라고 한대로 
        그대로 구현함 ㅋㅋ

        처음에 문제 설명이 이해가 안되서 살짝 뇌정지 왔었음 ㅋㅋㅋㅋㅋ
        근데 문제 자체는 디게 쉬운듯??
    '''

    answer = 0

    data.sort(key=lambda x: (x[col-1], -x[0]))

    print(data)

    for i in range(row_begin-1, row_end):

        total_mod = 0
        print(data[i])
        for num in data[i]:
            total_mod += (num % (i+1))
        
        answer = answer ^ total_mod

    return answer


print(solution(	[[2, 2, 6], [1, 5, 10], [4, 2, 9], [3, 8, 3]], 2, 2, 3))



from functools import reduce

def firstSolu(data, col, row_begin, row_end):

    '''
        다른 사람 풀이
        프로그래머스 다른 사람 풀이
        https://school.programmers.co.kr/learn/courses/30/lessons/147354/solution_groups?language=python3

        와우 ㅋㅋㅋ
        파이썬에도 reduce가 있었네 ㅋㅋ
        그리고 정말 파이써닉하게 잘 하신듯? ㅋㅋㅋㅋ
    '''

    data.sort(key = lambda x: (x[col-1], -x[0]))
    return reduce(lambda x, y : x ^ y, [sum(map(lambda x: x%(i+1), data[i])) for i in range(row_begin-1, row_end)])