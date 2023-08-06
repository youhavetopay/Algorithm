
'''
    프로그래머스 N개의 최소공배수
    여러개의 수가 주어지면 이 들의 최소공배수를 구하는 문제
'''

def solution(arr):

    '''
        나의 풀이

        나의 접근법
        숫자 크기도 얼마 안되고 숫자 수도 최대 15개라서
        그냥 dict에 곱하는 수를 전부 넣어주는 방식으로
        체크를 했는데 통과함 ㅋㅋ
    '''

    nums = {}

    i = 1
    while True:

        for num in arr:

            next_num = num*i

            if next_num in nums:
                nums[next_num] += 1

                if nums[next_num] == len(arr):
                    return next_num
            else:
                nums[next_num] = 1
        
        i += 1


def firstSolu(arr):

    '''
        다른 사람 풀이
        https://velog.io/@insutance/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4Python-N%EA%B0%9C%EC%9D%98-%EC%B5%9C%EC%86%8C%EA%B3%B5%EB%B0%B0%EC%88%98

        최소공배수를 누적해서?? 계속 구해나감
        
        최소공배수는 x * y // gcd(x, y)

        gcd 는 최대공약수
    '''

    from math import gcd

    answer = arr[0]

    for num in arr:
        answer = answer * num // gcd(answer, num)
    
    return answer