import heapq

def convertTimeToSecond(time):

    h, m, s = map(int, time.split(':'))

    s += m * 60
    s += h * 3600

    return s

def convertSecondToTime(s):

    h = s // 3600
    if h < 10:
        h = '0' + str(h)
    s = s % 3600
    m = s // 60
    if m < 10:
        m = '0' + str(m)
    s = s % 60
    if s < 10:
        s = '0' + str(s)

    return str(h) + ':' + str(m) + ':' + str(s)
    

def solution(play_time, adv_time, logs):

    '''
        나의 풀이(못품.. ㅠㅠ)
        영상시청 기록 중 광고 시청 시간 누적이 
        가장 높은 광고의 시작 시간을 구하는 문제?? 

        나의 접근법
        진짜 아예 못품...
        시간들을 전부 초로 환산한 다음
        시작시간 순으로 정렬해서 계산하려고 했는데
        시간초과는 물론이고 몇개 빼고 다 틀림 ....

        그래도 그 동안 시간초과가 있는 문제는 있었어도 
        아예 못 푼건 진짜....
        너무 어려움.. ㅠㅠㅠ
    '''

    play_time = convertTimeToSecond(play_time)
    adv_time = convertTimeToSecond(adv_time)

    if play_time == adv_time:
        return convertSecondToTime(0)
    
    second_logs = []
    for log in logs:
        start, end = log.split('-')

        start_second = convertTimeToSecond(start)
        end_second = convertTimeToSecond(end)
        adv_end_time = start_second + adv_time

        second_logs.append([start_second, end_second, adv_end_time])
    
    second_logs.sort(key=lambda x:x[0])

    print(second_logs)

    answer = 0
    max_play_time = 0
    for i in range(len(second_logs)):

        start, end, adv_end = second_logs[i]
        now_play_count = 0

        for j in range(len(second_logs)):
            n_start, n_end, _ = second_logs[j]
            if n_start <= adv_end <= n_end:
                now_play_count += 1
            
        
        if now_play_count > max_play_time and adv_end <= play_time:
            answer = start
            max_play_time = now_play_count

    
    return convertSecondToTime(answer)

# print(solution("02:03:55", "00:14:15", ["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"]))


def firstSolu(play_time, adv_time, logs):

    '''
        다른 사람 풀이
        https://dev-note-97.tistory.com/156

        카카오 풀이랑 요기 풀이랑 섞어서 해봄..

        진짜 문제 노답......
        DP에다가 누적합까지?? 응용해야 하는 문제인듯함..

        나는 애초에 접근 방법부터 잘못된듯.. ㅋㅋㅋㅋㅋㅋㅋ
    '''

    # 시간들을 초 단위로 바꿔주기
    play_time_sec = convertTimeToSecond(play_time)
    adv_time_sec = convertTimeToSecond(adv_time)

    # 시작시간과 종료시간들
    logs_start_sec = []
    logs_end_sec = []

    # 모든 구간을 초단위로 나타내기
    total_time = [0] * (play_time_sec + 1)

    # 로그들 넣어주기
    for log in logs:
        start, end = log.split('-')
        start, end = convertTimeToSecond(start), convertTimeToSecond(end)
        logs_start_sec.append(start)
        logs_end_sec.append(end)

        # 해당 위치(시간)에서 시청을 시작했으니 +1
        total_time[start] += 1

        # 해당 위치(시간)에서 시청을 종료했으니 -1
        total_time[end] -= 1
    
    # 시청 구간들의 시청자 수 넣어주기
    for i in range(1, len(total_time)):
        total_time[i] += total_time[i - 1]
    
    # 시청자 수의 누적합??을 위해 다시 넣어주기
    for i in range(1, len(total_time)):
        total_time[i] += total_time[i - 1]

    most_view = 0
    max_time = 0
    # 광고 재생이 가능한 시간부터 시작
    for i in range(adv_time_sec - 1, play_time_sec):

        # 구간의 시청자 수가 가장 많은 시간을 구하기
        if i >= adv_time_sec:
            if most_view < total_time[i] - total_time[i - adv_time_sec]:
                most_view = total_time[i] - total_time[i - adv_time_sec]
                max_time = i - adv_time_sec + 1
        else:
            if most_view < total_time[i]:
                most_view = total_time[i]
                max_time = i - adv_time_sec + 1

    return convertSecondToTime(max_time)

print(firstSolu("02:03:55", "00:14:15", ["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"]))