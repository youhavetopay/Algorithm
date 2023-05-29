from collections import deque

def solution(sequence, k):

    '''
        나의 풀이
        일정 수가 되는 수열의 구간을 찾는 문제

        나의 접근법
        deque를 사용해서 인덱스를 저장하고
        합도 따로 저장해서 계산함

        생각보다 쉬웠음..
    '''

    answer = []

    # 현재 수열의 합
    now_sum = 0
    # 현재 수열의 인덱스들
    queue = deque()

    for i, num in enumerate(sequence):
        
        # 현재 합이 넘었으면 앞에 숫자 빼주기
        while queue and now_sum + num > k:
            now_sum -= sequence[queue.popleft()]
    
        if now_sum + num < k:
            queue.append(i)
            now_sum += num

        elif now_sum + num == k:
            queue.append(i)
            now_sum += num
            answer.append([queue[0], queue[-1]])

    # 수열의 길이가 짧고 시작 숫자가 빠른 순으로
    answer.sort(key= lambda x: (x[1] - x[0], x[0]))

    return answer[0]

print(solution([1, 1, 1, 2, 3, 4, 5], 5))


def firstSolu(sequence, k):

    '''
        다른 사람 풀이
        프로그래머스 다른 사람 풀이
        https://school.programmers.co.kr/learn/courses/30/lessons/178870/solution_groups?language=python3

        누적합과 투포인터를 사용한 풀이
        솔직히 누적합이라길래 나보다 엄청 빠를줄 알았는데
        생각보다 그렇게 빠르진 않고 쪼~~~금 빠름..
        아마 투포인터로 찾는 과정이 나랑 동일한 과정을 거쳐서 그런듯??
    '''

    answer = []
    arr = [sequence[0]]

    # 누적합 구하기
    for i in range(1, len(sequence)):
        num = sequence[i] + arr[-1]
        arr.append(num)
    
    start = 0
    end = 0
    answer = None
    answer_idx = None
    cnt = 0

    # 투 포인터로 탐색
    while start <= end and end < len(sequence):
        s = arr[start]
        e = arr[end]
        val = e - s + sequence[start]

        if val == k:
            if answer is None:
                answer = [start, end]
            else:
                if (answer[-1] - answer[0]) > (end - start):
                    answer = [start, end]
        
        if start == end:
            end += 1
        elif val > k:
            start += 1
        else:
            end += 1
    
    return answer