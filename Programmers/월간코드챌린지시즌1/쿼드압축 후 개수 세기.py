def solution(arr):

    '''
        나의 풀이
        정사각형으로 이루어진 리스트가 있을때
        1로 이루어진 정사각형과 0과 이루어진 정사각형의 개수를 
        구하는 문제

        나의 접근법
        분할정복의 기본 문제라서 그렇게 어렵진 않았음
        그냥 현재 2차원 리스트가 같은 숫자로 이루어졌는지 체크하고
        같은 숫자로 이뤄져있으면 끝내고 아니면
        4분할로 나눠서 체크하는 방식으로 품
    '''

    answer = [0, 0]

    result, target = check(arr)
    if result:
        answer[target] += 1
        return answer

    first = []
    second = []
    for i in range(len(arr) // 2):
        first.append(arr[i][:len(arr)//2])
        second.append(arr[i][len(arr)//2:])
    
    third = []
    fourth = []
    for i in range(len(arr)//2, len(arr)):
        third.append(arr[i][:len(arr)//2])
        fourth.append(arr[i][len(arr)//2:])

    first_result = solution(first)
    second_result = solution(second)
    third_result = solution(third)
    fourth_result = solution(fourth)

    total_results = [first_result, second_result, third_result, fourth_result]

    for zero, one in total_results:
        answer[0] += zero
        answer[1] += one


    return answer

def check(now_arr):

    target = ''

    for nums in now_arr:
        for num in nums:
            if target == '':
                target = num
            elif target != num:
                return [False, target]
            
    return [True, target]


print(solution([[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]]))


def firstSolu(arr):

    '''
        다른 사람 풀이
        프로그래머스 다른 사람 풀이
        https://school.programmers.co.kr/learn/courses/30/lessons/68936/solution_groups?language=python3

        재귀로 했는데
        4분할로 나누는 부분을 아주 깔끔하게 표현하신듯? ㅋㅋ
        시작점을 x, y 로 주어지고 size만큼 반복하는 방법
        나중에 나도 이런 방식으로 풀면 좋을듯 함 ㅋㅋ
    '''

    answer = [0, 0]

    def check(size, x, y):
        if size == 1:
            answer[arr[y][x]] += 1
            return
        
        else:
            first = arr[y][x]

            for dy in range(size):
                for dx in range(size):
                    if first != arr[y + dy][x + dx]:
                        check(size // 2, x, y)
                        check(size // 2, x + size // 2, y)
                        check(size // 2, x, y + size // 2)
                        check(size // 2, x + size // 2, y + size // 2)
                        return
            
            answer[first] += 1
    
    check(len(arr), 0, 0)

    return answer