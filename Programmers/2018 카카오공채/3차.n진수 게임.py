def transNumber(number, arithmetic):

    alpha = ['A', 'B', 'C', 'D', 'E', 'F']

    trans_num = ''

    while number > 0:

        number, remain = divmod(number, arithmetic)

        if remain >= 10:
            trans_num += alpha[remain % 10]
        else:
            trans_num += str(remain)
        
    
    return trans_num[::-1]


def solution(n, t, m, p):

    '''
        나의 풀이
        숫자들을 해당 진법으로 변환한 후에
        해당 숫자를 한 자리수 씩 말하는게임에서 튜브의 t번째 턴까지 말할 숫자를 찾는 문제

        나의 접근법
        N진수 변환을 해야하므로 진수 변환 함수를 만들고
        문자열로 해서 길이를 사람 수 * 필요한 턴 까지의 숫자를 모두 구함
        그 다음 나의 턴만큼 짤라내고 필요한 턴까지 짤라내는 방식으로 품

        문제 자체는 그렇게 어렵진 않았는데 생각보다 오래걸림.. ㅋㅋ
    '''

    answer = ''

    nums = '0'

    now_num = 1
    while len(nums) < t * m:
        nums += transNumber(now_num, n)
        now_num += 1
    
    idx = p - 1
    answer = nums[idx::m]

    return answer[:t]

print(solution(2, 4, 2, 1))


big = ['A', 'B', 'C', 'D', 'E', 'F']

def firstSoul(n, t, m, p):

    '''
        다른 사람 풀이
        프로그래머스 다른 사람 풀이
        https://school.programmers.co.kr/learn/courses/30/lessons/17687/solution_groups?language=python3

        나랑 접근법이 똑같음
        필요 턴 * 사람 수 까지의 자리수를 구한 다음
        필요한 만큼 짤라서 반환

        대신 변수명이 짧아서 그런지 훨씬 간단해보임 ㅋㅋ
    '''

    a = '0'
    i = 0

    while True:
        if len(a) >= t*m:
            break

        b = ''
        j = i

        while (j):
            if j%n > 9:
                b = big[j%n-10] + b
            else:
                b = str(j%n) + b

            j = j // n
        
        a = a + b
        i = i + 1
    
    answer = a[p-1::m][:t]
    return answer
