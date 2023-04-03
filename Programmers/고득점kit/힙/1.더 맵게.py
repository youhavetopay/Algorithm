import heapq

def solution(scoville, K):

    '''
        나의 풀이
        heap을 이용해서 최소 값이 K가 될때까지 연산하는 횟수를 계산하는 문제

        파이썬의 heapq를 사용하면 아주 쉽게 풀수 있는 문제인듯 함

        이전에도 풀었던 적이 있는데 코드 형태??만 다르지 똑같이 heapq를 사용해서 품 ㅋㅋ
        차이점이라면 그때는 heapify를 몰라서 새로운 heap을 만들어서 사용했는데
        이번엔 heapify를 사용했다는 점??
    '''

    answer = 0
    heapq.heapify(scoville)

    while len(scoville) >= 2 and scoville[0] < K:

        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)

        heapq.heappush(scoville, first + (second * 2))

        answer += 1
    
    if len(scoville) < 2 and scoville[0] < K:
        return -1

    return answer


import collections

def firstSoul(scoville, K):

    '''
        다른 사람 풀이
        https://velog.io/@limeorange/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-Python-%EB%8D%94-%EB%A7%B5%EA%B2%8C

        deque를 활용한 풀이
        mix를 한 양념??과 기존 앙념을 각각에 큐에 담아서
        작은거 먼저 뽑아서 조합하는 방식으로 품
        deque를 사용한게 조금 신기함 ㅋㅋ
    '''

    answer = 0
    mix = collections.deque()
    
    scoville.sort()
    sco = collections.deque(scoville)

    while (sco and sco[0] < K) or (mix and mix[0] < K):

        answer += 1
        if len(sco) + len(mix) <= 1:
            return -1
        
        food = [0]*2
        for a in range(2):
            if sco and mix:
                if sco[0] < mix[0]:
                    food[a] = sco.popleft()
                else:
                    food[a] = mix.popleft()
            
            elif sco:
                food[a] = sco.popleft()
            else:
                food[a] = mix.popleft()
        
        mix.append(food[0] + food[1]*2)

    return answer