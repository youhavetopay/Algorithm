from collections import Counter, defaultdict

def solution(topping):

    '''
        나의 풀이
        숫자 리스트가 있을때 
        2개로 나누었을때 숫자 종류가 같게 나오는 나누는 경우의 수를
        구하는 문제

        나의 접근법
        처음엔 큐 두개로 넣고 빼고 하면서
        set으로 비교했는데 시간초과 뜸 ㅋㅋㅋㅋ

        그래서 생각해봤는데 종류도 카운팅하고 
        총 개수도 셀수 있는 방법을 생각해봤는데
        처음에 Counter로 전부 세고 하나씩 빼는 방법으로 하니까 풀림 ㅋㅋ

        생각보다 어려운 문제였음 ㅋㅋ
    '''

    answer = 0

    left = defaultdict(int)
    right = Counter(topping)

    for i in range(len(topping)):

        left[topping[i]] += 1
        right[topping[i]] -= 1

        if right[topping[i]] == 0:
            del right[topping[i]]
        
        if len(left) == len(right):
            answer += 1
        

    return answer

print(solution([1, 2, 1, 3, 1, 4, 1, 2]))


def firstSolu(topping):

    '''
        다른 사람 풀이
        프로그래머스 다른 사람 풀이
        https://school.programmers.co.kr/learn/courses/30/lessons/132265/solution_groups?language=python3

        이진탐색 두번의 결과값을 
        바탕으로 정답을 찾음?? 

        이게 무슨원리임?? ㅋㅋㅋㅋ
    '''

    answer = 0

    l, r = 0, len(topping)
    idx1 = 0
    while l <= r:
        m = (l + r) // 2
        left = len(set(topping[:m]))
        right = len(set(topping[m:]))

        if left < right:
            l = m + 1
        elif left >= right:
            idx1 = m
            r = m - 1
    
    l, r = 0, len(topping)
    idx2 = 0
    while l <= r:
        m = (l + r) // 2
        left = len(set(topping[:m]))
        right = len(set(topping[m:]))

        if left <= right:
            idx2 = m
            l = m + 1
        elif left > right:
            r = m - 1
    
    answer = max(idx2 - idx1 + 1, 0)
    return answer