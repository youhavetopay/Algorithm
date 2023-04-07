import itertools

def makePrimeNumbers(numbers):

    length = int(''.join(sorted(list(numbers), reverse=True))) + 1

    nums = [True] * length

    for i in range(2, int(length ** 0.5) + 1):
        if nums[i]:
            for j in range(i+i, length, i):
                nums[j] = False
    
    return nums


def solution(numbers):

    '''
        나의 풀이
        숫자들의 순열?? 으로 해당 숫자가 소수 인지 판별하는 문제

        파이썬에 순열을 구해주는 라이브러리가 있어서 그나마..쉽게 풀었음

        처음에 문제를 잘못보고 조합인줄 알고 DFS로 직접 구현했는데
        순열인거 보고 식겁함 ㅋㅋㅋㅋㅋㅋ
        그리고 에라토스테네스의 체를 잘못 구현해서 
        결국 위키를 보고 품 ㅋㅋ
    '''

    prime_numbers = set()
    prime_number_table = makePrimeNumbers(numbers)
    
    for i in range(1, len(numbers)+1):

        for num in set(map(''.join, itertools.permutations(numbers, i))):
            if int(num) > 1 and prime_number_table[int(num)]:
                prime_numbers.add(int(num))


    return len(prime_numbers)


print(solution("011"))


def firstSoul(n):

    '''
        다른 사람 풀이
        https://velog.io/@nayoon-kim/%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%97%B0%EC%82%B0%EC%9E%90

        전체적인 로직은 나랑 비슷함

        set에서 중복 및 빼기 연산이 된다는 걸 활용해서
        참 파이써닉하게 풀어낸 풀이 같음
    '''

    a = set()

    # 모든 길이에 따른 순열 구하기
    for i in range(len(n)):
        # | 은 병합 연산자 (대충 유니온??)
        a |= set(map(int, map("".join, itertools.permutations(list(n), i+1))))
    
    # 0, 1 빼기
    a -= set(range(0, 2))

    # 에라토스테네스의 체 구해서
    # 소수 아닌거 빼주기
    for i in range(2, int(max(a) ** 0.5) + 1):
        a -= set(range(i * 2, max(a) + 1, i))

    # 남은건 전부 소수임 ㅋㅋ
    return len(a)