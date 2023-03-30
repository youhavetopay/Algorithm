import collections, math

def solution(progresses, speeds):

    '''
        나의 풀이
        큐를 활용한 구현 문제

        큐를 안다면 쉬운 문제라고 생각되는 문제였음
        처음엔 그냥 완료되는데로 바로 빼야하는줄 알고 했는데
        그게 아니라 앞 작업이 끝나야 뒷 작업도 빠질 수 있어서
        그냥 큐를 구현하면 되는 거 였음 ㅋㅋㅋ
    '''

    answer = []

    # [작업 진행도, 개발 속도] 이렇게 queue에 넣어둠
    queue = collections.deque([[job, speed] for job, speed in zip(progresses, speeds)])
    
    # queue에 모든 작업이 끝날때 까지 반복
    while len(queue) > 0:

        print(queue, answer)

        # 첫번째 작업의 완료되기 까지의 걸리는 시간 계산
        job, speed = queue[0]
        need_day = math.ceil((100 - job) / speed)

        # 모든 작업에 첫번째 작업이 완료되기 까지 걸리는 시간에 따라
        # 다 더해줌
        for idx in range(len(queue)):
            job, speed = queue[idx]
            queue[idx] = [job + (speed * need_day), speed]
        
        # 맨 앞에 작업이 끝났다면 빼주고
        # 카운트 하기
        done = 0
        while queue and queue[0][0] >= 100:
            queue.popleft()
            done += 1
        
        # 카운트 한거 정답 리스트에 넣어주기
        answer.append(done)
            
    return answer

print(solution([93, 30, 55], [1, 30, 5]))


def firstSoul(progresses, speeds):

    '''
        다른 사람 풀이
        https://huidea.tistory.com/15

        처음에 작업이 완료되는 시간을 미리 다 구해놓고
        
        지역 최대 값????을 찾고 
        더 큰 최대값을 찾을 때까지 계속 탐색
        없다면 해당 작업이 완료되기 전까지 아무도 빠져나가지 못하니까
        계산해서 넣어줌

        조금 헷갈리게 푼듯?? 그래도 시간복잡도는 훨씬 낮을듯?????

        근데 다들 풀이를 보면 queue를 안쓰고 품 ㅋㅋㅋ
        그냥 queue 쓰라구 ㅋㅋㅋ
    '''

    # 미리 계산
    progresses = [math.ceil((100-a) / b) for a, b in zip(progresses, speeds)]
    answer = []

    front = 0

    for idx in range(len(progresses)):
        if progresses[idx] > progresses[front]:
            answer.append(idx - front)
            front = idx
    
    answer.append(len(progresses) - front)

    return answer