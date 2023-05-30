def solution(plans):

    '''
        나의 풀이 (살짝 억지로 통과한듯.. ㅋㅋㅋ)
        우선순위큐와 스택을 혼합한 문제?? 
        과제를 진행하다가 다른 과제를 진행할 시간이되었다면
        해당 과제를 진행하고 다시와서 마저하는 과정을 거칠때
        과제를 먼저 마치는 순서를 구하는 문제

        나의 접근법 (좀 뻘짓함..ㅋㅋ)
        효율성 생각안하고 막 한거라서 좀 풀이가 복잡함 ㅋㅋㅋ

        일단 작업 시작시간을 기준으로 정렬해서
        dict 자료형에 담아두고
        dict 자료형이 비워질때까지 반복하면서 현재 해야하는 과제이름을 찾고
        진행하는 방식으로 구현함

        지금보니까 힙이랑 스택으로 구현했으면 훨씬 편하고 빨랐을듯...ㅠㅠ
        진짜.. 생각좀 하고 풀자..으이구!!
    '''

    answer = []

    time_plans = {}

    # 시작 시간으로 정렬
    plans.sort(key=lambda x: convertTimeToMinute(x[1]))

    # dict에 시작시간이랑 과제를 완료하는데 남은 시간을 저장
    for i in range(len(plans)):
        name, start_time, cost = plans[i]
        start_time = convertTimeToMinute(start_time)
        cost = int(cost)

        time_plans[name] = [start_time, cost]
    
    wating = []
    now_processing = plans[0][0]
    now_time = time_plans[now_processing][0]

    # 모든 과제를 끝낼때 까지
    while time_plans:

        # 현재 처리하고 있는 과제의 남은 시간
        now_cost = time_plans[now_processing][1]
        # 이 과제를 끝내는 시간
        finish_time = now_time + now_cost

        # 남은 과제들 중에서 탐색
        for name, [start_time, cost] in time_plans.items():
            # wating에 들어가 있지 않고 
            # 현재 작업이 아니고 
            # 과제 완료시간 보다 시작시간이 짧은 과제를 찾음
            if name not in wating and name != now_processing and finish_time > start_time:
                # 현재 진행하고 있는건 wathing 에 넣어주기
                wating.append(now_processing)
                # 남은 과제 시간 계산
                time_plans[now_processing][1] -= start_time - now_time
                # 다음 진행해야하는 과제
                now_processing = name
                now_time = start_time
                
                # 파이썬은 dict 자료형이 넣은 순서를 보장하기 때문에
                # 여기서 반복문을 끝내면 됨
                break
        else:
            # 만약 다음 과제 시작 시간 전까지 현재 과제를 끝낼 수 있을 때
            # 현재 과제 완료해주기
            now_time = finish_time
            answer.append(now_processing)
            del time_plans[now_processing]

            # 다음 과제 탐색
            for i, [name, [start_time, cost]] in enumerate(time_plans.items()):
                if (not wating and now_time < start_time) or (name not in wating and now_time == start_time):
                    now_processing = name
                    now_time = start_time
                    break
                
            else:
                # 할게 없다면 wathing에 넣어둔거 마저 진행하기
                if wating:
                    now_processing = wating.pop()


        print(now_processing,now_time, wating, time_plans)

    return answer

def convertTimeToMinute(time):

    h, m = map(int, time.split(':'))
    m += h * 60

    return m

print(solution([['A', "12:00", "30"], ['B', "12:10", "20"], ['C', "15:00", "40"], ['D', "15:10", "30"]]))


def firstSolu(plans):

    '''
        다른 사람 풀이
        프로그래머스 다른 사람 풀이
        https://school.programmers.co.kr/learn/courses/30/lessons/176962/solution_groups?language=python3

        대박 ㅋㅋㅋㅋㅋㅋㅋ
        해당 과제을 나중에 해야한다면
        진행해야하는 과제의 진행 시간을 더해주고
        마지막에 정렬...
        대박......

        그리고 람다 참 잘 사용하시는듯.. ㅋㅋㅋ
    '''
    # 시간을 분으로 바꾸고 숫자로 만들기
    plans = sorted(map(lambda x: [x[0], int(x[1][:2]) * 60 + int(x[1][3:]), int(x[2])], plans), key=lambda x: -x[1])

    lst = []
    while plans:
        x = plans.pop()
        for i, v in enumerate(lst):
            # 종료시간이 시작시간보다 늦을 때
            if v[0] > x[1]:
                # 걸리는 시간을 더해주기
                lst[i][0] += x[2]
        
        # 시작시간 + 걸리는 시간 => 종료시간
        lst.append([x[1] + x[2], x[0]])
    
    # 종료시간이 빠른 순서대로 정렬
    lst.sort()

    return list(map(lambda x: x[1], lst))