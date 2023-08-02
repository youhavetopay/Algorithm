
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
