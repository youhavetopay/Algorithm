import collections
import heapq

def solution(jobs):

    '''
        나의 풀이
        작업들의 평균 처리 시간을 계산하는 문제

        정렬과 heapq를 사용하면 풀 수 있는 문제인듯 함 ㅋㅋ

        문제 푸는데 좀 오래걸렸는데
        그 이유가 좀 한심함 ㅋㅋㅋㅋㅋ

        작업들이 시간에 맞춰서 정렬되지 않는다는 걸 알면서도
        정렬이 된 걸 기준으로 풀고 있어서 푸는데 한참 걸림 ㅋㅋㅋㅋㅋ
    '''

    # 평균시간
    answer = 0
    
    # 도착한 시간에 따른 작업들
    time_table = collections.defaultdict(list)

    # 도착한 순서대로 정렬
    # 이거 안해줘서 ....
    jobs.sort(key=lambda x:x[0])

    # 도착한 시간을 기준으로
    # 작업에 걸리는 시간을 넣어줌 -> 시간이 짧은거 먼저 나오도록
    for arrive, end in jobs:
        heapq.heappush(time_table[arrive], end)

    # 현재 시간
    now_time = 0

    # 모든 작업을 끝낼때 까지
    while time_table.keys():
        
        # 현재 시간에 할수 있는 작업들
        can_jobs = []
        for key, values in time_table.items():
            
            # 도착한 시간이 현재 시간 이전인 경우
            if key <= now_time:
                can_jobs.append([key, values[0]])
            else:
                break
        
        # 현재 할 수 있는 작업이 없을 때
        if not can_jobs:
            now_time += 1
            continue
        
        # 작업시간이 짧은걸로 정렬
        can_jobs.sort(key=lambda x:(x[1]))
        arrive, end = can_jobs[0]
        heapq.heappop(time_table[arrive])

        # 해당 시간에 도착한 작업이 모두 끝났을 때
        if not time_table[arrive]:
            del time_table[arrive]
        
        # 시간 계산
        answer += (now_time-arrive) + end
        now_time += end

    # 소수점은 버리고 평균을 계산
    return int(answer / len(jobs))


print(solution([[24, 10], [18, 39], [34, 20], [37, 5], [47, 22], [20, 47], [15, 34], [15, 2], [35, 43], [26, 1]]))


def firstSoul(jobs):
    
    '''
        다른 사람 풀이
        https://velog.io/@younge/Python-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EB%94%94%EC%8A%A4%ED%81%AC-%EC%BB%A8%ED%8A%B8%EB%A1%A4%EB%9F%AC-%ED%9E%99

        코드가 짧고 간결하면서 heap만 사용해서 너무 예뻤음 ㅋㅋ
        나랑 얼추 비슷하면서도 약간 다름 ㅋㅋ
        할 수 있는 작업이 없을때 1씩 올리는 것?

        대신 정렬을 사용을 안해서 훨씬 빠름 ㅋㅋ

        
        현재 시점에서 처리할 수 있는 작업들을 힙에 넣고,
        하나를 뽑아 현재 시점과 총 대기시간을 구해주는 방식??
    '''

    answer, now, i = 0, 0 ,0
    start = -1
    heap = []

    while i < len(jobs):

        for j in jobs:

            # 작업 요청 시간이 
            # 최근에 완료한 작업의 시작시간보다 크고
            # 현재 시점보다 작을때 heap에 넣음
            # -> 할 수 있는 작업
            if start < j[0] <= now:
                heapq.heappush(heap, [j[1], j[0]])
        
        if len(heap) > 0:
            current = heapq.heappop(heap)
            start = now
            now += current[0]
            answer += (now - current[1])
            i += 1
        
        else:
            now += 1
        
    
    return int(answer / len(jobs))