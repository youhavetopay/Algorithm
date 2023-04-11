def solution(numbers, target):

    '''
        나의 풀이
        숫자들의 합과 빼기로 목표 숫자를 만드는 경우의 수 구하는 문제

        깊이/너비 우선 탐색 유형이라고 하는데
        그냥 모든 경우의수 찾는 방법으로 품 ㅋㅋ
        그래서 조금 오래걸리는듯??

        이전에도 푼 적 있는데
        이전풀이는 너무 복잡한 대신에 이거보다 약 2배정도 빠름 ㄷㄷㄷ
    '''

    answer = 0

    # 최대 길이
    length = len(numbers)

    # 더하기, 빼기 조합 구하기
    def makeExpression(nums):

        # 모든 숫자들에 대한 더하기, 빼기 조합을 구했을 때
        if len(nums) == length:

            # 계산
            numbers_sum = 0
            for idx, num in enumerate(nums):
                numbers_sum += (numbers[idx] * num)

            # 목표 숫자라면 1 아니면 0
            if numbers_sum == target:
                return 1
            
            return 0
        
        temp = 0

        # 1(더하기), -1(빼기) 조합 구하기
        for i in [1, -1]:
            temp += makeExpression(nums + [i])

        return temp

    answer = makeExpression([])

    return answer

print(solution([1, 1, 1, 1, 1], 3))


def firstSoul(numbers, target):

    '''
        다른 사람 풀이
        프로그래머스 다른 사람 풀이
        https://school.programmers.co.kr/learn/courses/30/lessons/43165/solution_groups?language=python3

        재귀함수로 품 ㄷㄷ ㅋㅋㅋ

        numbers의 첫번째 숫자를 더하거나 빼서 target을 업데이트 하고
        나머지 배열로 다시 찾아가는 방식으로 구현 ㄷㄷㄷ

        시간복잡도도 내꺼의 거의 9배?? 정도 빠름 ㅋㅋㅋㅋㅋㅋ
        코드 자체도 디게 깔끔하고 좋은듯 함 ㅋㅋㅋ

    '''

    if not numbers and target == 0:
        return 1
    elif not numbers:
        return 0
    
    else:
        return firstSoul(numbers[1:], target - numbers[0]) + firstSoul(numbers[1:], target + numbers[0])