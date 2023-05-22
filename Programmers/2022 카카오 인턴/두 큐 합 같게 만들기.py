from collections import deque

def solution(queue1, queue2):
    
    '''
        나의 풀이
        두 큐의 합이 같아질때까지
        pop 과 insert를 반복하는 횟수를 계산하는 문제
        
        나의 접근법
        그냥 큐 두개 만들고
        합이 큰 곳에서 작은곳으로 pop과 insert를 해줬고
        두 큐의 길이 * 2 만큼 반복했는데도 못하면 끝내는 방식으로 품
        
        처음엔 엄청 어렵겠다 라고 생각했었는데
        막상하니까 너무 어이없게?? 풀려서 좀 허무 했음.. ㅋㅋ
        처음엔 두 큐의 길이까지 만큼 체크했는데
        1번케이스 안풀리길래 그냥 단순히 제한만 늘렸는데
        통과해서 그런지 더 어이없었음 ㅋㅋㅋㅋ
    '''
    
    answer = 0
    
    a_sum, b_sum = sum(queue1), sum(queue2)
    
    total_length = len(queue1) + len(queue2)
    
    total = a_sum + b_sum
    
    a_q = deque(queue1)
    b_q = deque(queue2)
    
    if total % 2 != 0:
        return -1
    
    while a_sum != b_sum:
        
        if a_sum > b_sum:
            a = a_q.popleft()
            a_sum -= a
            b_sum += a
            b_q.append(a)
        else:
            b = b_q.popleft()
            a_sum += b
            b_sum -= b
            a_q.append(b)
            
        answer += 1
        
        if answer > total_length * 2 or not a_q or not b_q:
            return -1
    
    return answer

def firstSolu(que1, que2):
    
    '''
        다른 사람 풀이
        프로그래머스 다른 사람 풀이
        https://school.programmers.co.kr/learn/courses/30/lessons/118667/solution_groups?language=python3
        
        투포인터??를 활용한 풀이 인듯 함
        대충 que1의 합으로 시작해서 넣고 빼고를 반복하는 방식인듯
        근데 살짝 이해 안가는건
        왜 que1의 길이의 2배까지만 체크하는건지 이해가 잘 안감..
        
        다른 사람들 풀이에 따르면
        하나의 큐의 요소가 다른큐에 전체 이동하고 다시 원래대로 
        돌아오는데 큐 길이의 * 3 까지 라고 함
        아마 시간초과가 걸리지 않게 적당량만 설정해주면 
        그리디 문제라서 쉽게 풀린다고 함
    '''
    
    queSum = sum(que1) + sum(que2)
    
    if queSum % 2:
        return -1
    
    target = queSum // 2
    
    n = len(que1)
    start = 0
    end = n - 1
    ans = 0
    
    cur = sum(que1)
    que3 = que1 + que2
    
    while cur != target:
        if cur < target:
            end += 1
            if end == n * 2:
                return -1
            
            cur += que3[end]
        else:
            cur -= que3[start]
            start += 1
        
        ans += 1
    
    return ans
