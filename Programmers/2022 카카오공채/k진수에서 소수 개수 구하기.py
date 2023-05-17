def trans_number(n, k):

    if k == 10:
        return str(n)

    nums = ''

    while n >= 3:

        num = n % k
        nums += str(num)
        n = n // k
    
    nums += str(n)

    return nums[::-1]

def split_num(trans_num):

    nums = []

    now_num = ''
    for w in trans_num:
        if w == '0':
            if now_num:
                nums.append(int(now_num))
                now_num = ''
        else:
            now_num += w

    if now_num:
        nums.append(int(now_num))

    return nums

    


def is_prime_number(num):

    i = 2
    if num < i:
        return False
    
    while i < num ** (1/2):

        if num % i == 0:
            return False
        
        i += 1

    
    return True


def solution(n, k):
    
    '''
        나의 풀이
        숫자를 K진수로 변환한 다음 나온 숫자들이 
        소수인지 판별하는 문제

        나의 접근법
        처음에 소수구하는 방법을 에라토스테네스의 체로 구했는데
        런타임 에러가 발생했었음
        확인해보니까 특정 케이스에서는 12억까지 구해야하는 부분이 있어서
        모든 소수를 구하는 것이 아닌 해당 수가 소수인지만 판별을 해야하고
        소수 구하는 알고리즘은 O(n)이 되면 안된다고 했었음
        그래서 찾아보니 O(n ** (1/2)) 알고리즘이 있어서
        그걸로 하니 풀렸음..

        소수구하는 알고리즘을 잘 안다면 쉽게 풀리는 문제인듯..
    '''

    answer = 0

    trans_n = trans_number(n, k)
    
    nums = split_num(trans_n)

    for num in nums:
        if is_prime_number(num):
            answer += 1

    return answer

print(solution(7971161, 3))



def conv(n, k):

    s = ''
    while n:
        s += str(n%k)
        n //= k
    
    return s[::-1]

def isprime(n):
    if n <= 1: return False

    i = 2
    while i*i <= n:
        if n%i == 0: return False
        i += 1
    
    return True

def firstSolu(n, k):

    '''
        다른 사람 풀이
        프로그래머스 다른 사람 풀이
        https://school.programmers.co.kr/learn/courses/30/lessons/92335/solution_groups?language=python3

        풀이법은 나랑 똑같음
        근데 split을 사용했다는 점이 다름 ㅋㅋ
        처음에 나도 split 사용했었는데 에러떠서 직접 구현했는데
        그냥 continue하면 되는거였네.. ㅋㅋㅋㅋ
    '''

    s = conv(n, k)
    cnt = 0

    for num in s.split('0'):
        if not num: continue
        if isprime(int(num)): cnt += 1

    return cnt