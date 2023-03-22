from typing import List
import heapq
import datetime

def solution(lines: List[str]):

    '''
        나의 풀이 (못품 ㅠㅠ)

        특정 구간 시간에 처리량을 구하는 문제

        시작시간을 구해서 heap으로 풀어볼려고 했는데
        특정 시점이 아닌 1초동안 처리하고 있는 량을 구해야하는 문제라서
        너무 어려웠음 ㅠㅠ

        애초에 접근법이 잘못된듯..
    '''

    answer = 0

    log_times = []

    # 종료시간과 처리 시간으로 시작시간을 구함
    # 시간을 전부 초 단위로 변경함
    for line in lines:
        date, end_time, time = line.split(' ')

        year, month, day = date.split('-')
        day = int(day)

        h, m, s = end_time.split(':')
        h, m, s = int(h), int(m), float(s)

        time = round(float(time[:-1]) - 0.001, 3)

        end_time_second = s
        end_time_second += (m * 60)
        end_time_second += (h * 60 * 60)
        end_time_second += (day * 60 * 60 * 24)
        
        log_times.append([round(end_time_second - time, 3), end_time_second])


    
    # 시작시간을 기준으로 정렬
    log_times.sort(key=lambda x: x[0])

    for i, t in enumerate(log_times):
        print(i+1,t)


    # heap으로 해당 시점에 처리량을 구하는 건 가능하지만
    # 특정 시점에서의 1초동안 처리량은 구하기 힘든 것 같음..
    heap = []
    for start, end in log_times:
        heapq.heappush(heap, end)

        while heap and heap[0] < start:
            heapq.heappop(heap)
        
        print(start, len(heap))
        answer = max(answer, len(heap))


    return answer


print(solution([
"2016-09-15 20:59:57.421 0.351s",
"2016-09-15 20:59:58.233 1.181s",
"2016-09-15 20:59:58.299 0.8s",
"2016-09-15 20:59:58.688 1.041s",
"2016-09-15 20:59:59.591 1.412s",
"2016-09-15 21:00:00.464 1.466s",
"2016-09-15 21:00:00.741 1.581s",
"2016-09-15 21:00:00.748 2.31s",
"2016-09-15 21:00:00.966 0.381s",
"2016-09-15 21:00:02.066 2.62s"
]))



def firstSoul(lines: List[str]):

    '''
        책 풀이
        슬라이딩 윈도우를 활용한 풀이
        디게 어려운 문제라서
        저자도 이러한 간결한 풀이를 위해 많은 고민을 했다고 함..
        정답율도 가장 낮게 기록했다고 함
    '''

    combined_lgos = []

    # 로그를 전부 초로 변경
    for log in lines:

        logs = log.split(' ')
        timestamp = datetime.datetime.strptime(logs[0] + ' ' + logs[1], 
                                               "%Y-%m-%d %H:%M:%S.%f").timestamp()
        
        # 종료시간은 -1
        combined_lgos.append((timestamp, -1))
        # 시작시간은 1로 구분
        combined_lgos.append((timestamp - float(logs[2][:-1]) + 0.001, 1))

    # 아직 종료되지 않은 요청 수
    accumulated = 0

    # 최대 처리량
    max_requests = 1

    # 시간 순으로 정렬
    combined_lgos.sort(key= lambda x: x[0])

    for i, elem1 in enumerate(combined_lgos):
        current = accumulated

        for elem2 in combined_lgos[i:]:
            # 최초 비교 시간이랑 시간이 1초 넘어가면 끝내기
            if elem2[0] - elem1[0] > 0.999:
                break
            
            # 요청이 시작된 시간인 경우
            if elem2[1] > 0:
                current += elem2[1]
        
        max_requests = max(max_requests, current)
        accumulated += elem1[1]

    return max_requests

print(firstSoul([
"2016-09-15 20:59:57.421 0.351s",
"2016-09-15 20:59:58.233 1.181s",
"2016-09-15 20:59:58.299 0.8s",
"2016-09-15 20:59:58.688 1.041s",
"2016-09-15 20:59:59.591 1.412s",
"2016-09-15 21:00:00.464 1.466s",
"2016-09-15 21:00:00.741 1.581s",
"2016-09-15 21:00:00.748 2.31s",
"2016-09-15 21:00:00.966 0.381s",
"2016-09-15 21:00:02.066 2.62s"
]))