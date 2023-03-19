import collections
from typing import List


def caculatorTime(start_time, n, t):

    bus_times = [start_time]
    h, m = map(int, start_time.split(':'))

    
    for i in range(n):
        if (m + t) // 60 > 0:
            h += 1
            m = (m + t) % 60

        else:
            m += t
        
        bus_times.append(str(h).zfill(2) + ':' +str(m).zfill(2))

    return bus_times

def getOneminit(max_time):

    h, m = map(int, max_time.split(':'))

    if m == 0:
        h -= 1
        m = 59
    else:
        m -= 1
    
    return str(h).zfill(2) + ":" + str(m).zfill(2)


def solution(n, t, m, timetable):

    '''
        나의 풀이 ㅋㅋㅋㅋㅋ
        알고리즘따위 1도 생각안하고 극한의 구현 ㅋㅋㅋㅋ
        이렇게 했는데 통과한것도 신기하네 ㅋㅋㅋ
    '''

    answer = '1111111111111'

    # 크루들이 도착한 시간 순으로 정렬해서 queue에 넣기
    timetable.sort()
    timetable = collections.deque(timetable)
    

    # 셔틀의 출발시간을 모두 계산해서 리스트에 담기
    start_time = '09:00'
    bus_times = caculatorTime(start_time, n-1, t)

    # 셔틀 시간에 따른 타는 사람들 넣기
    bus_table = collections.defaultdict(list)

    for bus_time in bus_times:

        bus_h, bus_m = map(int, bus_time.split(':'))
        for crew_time in list(timetable):
            crew_h, crew_m = map(int, crew_time.split(':'))

            # 시간 계산해서 해당 버스에 탈 수 있는 사람들을 
            # popleft로 넣어주기
            # 단 최대 인원 안넘어가게
            if len(bus_table[bus_time]) < m:

                if crew_h < bus_h:
                    bus_table[bus_time].append(timetable.popleft())
                
                elif crew_h == bus_h and crew_m <= bus_m:
                    bus_table[bus_time].append(timetable.popleft())
                    
                else:
                    break
            else:
                break
        
    print(bus_table)

    # 최대 시간을 구하기 위해서
    # 셔틀 출발시간이 가장 느린것 부터
    for bus_time in reversed(bus_times):
        # 셔틀에 바로 탈 수 있으면 셔틀 출발시간이 정답
        if len(bus_table[bus_time]) < m:
            return bus_time
        
        # 바로 못타면
        # 현재 대기열의 최대값의 -1 분 시간을 구하기
        my_time = getOneminit(max(bus_table[bus_time]))

        # 나보다 앞에 있는 사람의 수를 구하기
        count = 0
        for time in bus_table[bus_time]:
            if time <= my_time:
                count += 1

        # 나까지 탈 수 있으면 해당 시간 반환
        if count < m:
            return my_time
            
    return answer


n2 = 2
t2 = 10
m2 = 2
timeTable2 = ["09:10", "09:09", "08:00"]


n3 = 2
t3 = 1
m3 = 2
timeTable3 = ["09:00", "09:00", "09:00", "09:00"]

n4 = 1
t4 = 1
m4 = 5
timeTable4 = ["00:01", "00:01", "00:01", "00:01", "00:01"]

print(solution(n4, t4, m4, timeTable4))


def firstSoul(n: int, t: int, m: int, timetable: List[str]) -> str:
    
    '''
        책 풀이

        역시 코드가 디게 깔끔함 ㅋㅋㅋ
        딱히 알고리즘이 필요한 문제는 아니였지만
        계산할것도 많고 빡 구현 문제라서 정답율이 두번째로 낮았다고 함
    '''

    # 크루들의 도착시간을 전부 분으로 변경
    timetable = [
        int(time[:2]) * 60 + int(time[3:])
        for time in timetable
    ]
    # 정렬
    timetable.sort()

    # 셔틀의 출발시간 -> 9시
    current = 540


    # 처음부터 반복을 하면서
    # 가장 느린시간을 구하기
    for _ in range(n):
        for _ in range(m):
            # 기다리고 있는 크루들 중 가장 앞에 있는 크루의 도착시간이
            # 셔틀 출발시간보다 앞일 때
            if timetable and timetable[0] <= current:
                # 해당 크루의 시간의 -1 분 
                candidate = timetable.pop(0) - 1
            else:
                # 앞에 기다리고 있는 크루가 없을 때
                candidate = current
        # 다음 셔틀 시간
        current += t

    # 00:00 형식으로 변환하기
    h, m, = divmod(candidate, 60)
    return str(h).zfill(2) + ':' + str(m).zfill(2)
