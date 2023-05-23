def convertTimeToDay(time):

    y, m, d = map(int, time.split('.'))

    d += m * 28

    d += y * 12 * 28

    return d

def convertMonthToDay(month):
    return int(month) * 28


def solution(today, terms, privacies):

    '''
        나의 풀이
        유효기간을 체크하는 문제

        나의 접근법
        모든 달이 28일까지 있다고 해서
        그냥 시간을 일 단위로 전부 변환해서
        체크함

        이거 예전에 풀었을때는 디게 어렵게 풀었는데
        시간 단위를 바꾸니까 훨씬 간단하게 풀수 있는듯???
    '''

    answer = []

    today_day = convertTimeToDay(today)
    terms_day = {}

    for info in terms:
        kind, month = info.split()
        terms_day[kind] = convertMonthToDay(month)
    
    for i, privacie in enumerate(privacies):
        time, kind = privacie.split()
        day = convertTimeToDay(time)
        max_day = terms_day[kind]

        print(time, day+max_day, today_day)
        if day + max_day - 1 < today_day:
            answer.append(i+1)

    return answer



def to_days(date):
    year, month, day = map(int, date.split("."))
    return year * 28 * 12 + month * 28 + day

def solution(today, terms, privacies):
    
    '''
        다른 사람 풀이
        프로그래머스 다른 사람 풀이
        https://school.programmers.co.kr/learn/courses/30/lessons/150370/solution_groups?language=python3

        나랑 비슷하게 일 단위로 바꿔서 하신듯..?
    '''

    months = {v[0]: int(v[2:]) * 28 for v in terms}
    today = to_days(today)
    expire = [
        i + 1 for i, privacy in enumerate(privacies)
        if to_days(privacy[:-2]) + months[privacy[-1]] <= today
    ]
    return expire