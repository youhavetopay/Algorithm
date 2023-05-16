from collections import defaultdict

def solution(id_list, report, k):

    
    '''
        나의 풀이
        내가 신고한 결과를 반환하는 문제

        나의 접근법
        그냥 내가 신고한거랑 신고된 사람의 신고된 횟수를 
        전부 비교하는 방식으로 품

        데이터 수가 많지 않아서 쉽게 풀리는듯?? ㅋㅋㅋ
    '''

    answer = []

    do_report = defaultdict(list)
    get_report = defaultdict(list)


    for ids in report:
        user, bad_user = ids.split()

        if bad_user not in do_report[user]:
            do_report[user].append(bad_user)
        
        if user not in get_report[bad_user]:
            get_report[bad_user].append(user)
    
    for user in id_list:

        count = 0
        for report_users in do_report[user]:
            if len(get_report[report_users]) >= k:
                count += 1
        
        answer.append(count)
    
    return answer

print(solution(["con", "ryan"], ["ryan con", "ryan con", "ryan con", "ryan con"], 3))


def firstSolu(id_list, report, k):
    
    '''
        다른 사람 풀이
        프로그래머스 다른 사람 풀이

        https://school.programmers.co.kr/learn/courses/30/lessons/92334/solution_groups?language=python3

        report 기록들을 set으로 중복을 없애는게
        가장 좋은듯.. ㅋㅋㅋㅋㅋ
    '''

    answer = [0] * len(id_list)
    reports = {x : 0 for x in id_list}

    for r in set(report):
        reports[r.split()[1]] += 1
    
    for r in set(report):
        if reports[r.split()[1]] >= k:
            answer[id_list.index(r.split()[0])] += 1

    return answer