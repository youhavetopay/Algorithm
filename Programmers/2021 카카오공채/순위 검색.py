import bisect

def solution(info, query):

    '''
        나의 풀이
        조건에 해당하는 사람의 수를 찾는 문제

        나의 접근법
        이것도 풀이법을 보고 한거라서 내가 혼자서 푼건 아님..ㅠㅠ
        구현은 쉬운 문제이지만 효율성을 통과하기 매우 어려웠던 문제였음

        조합별로 해시테이블을 미리 만들어두고
        해당 해시테이블에 해당하는 사람들의 점수를 넣어둠
        그 후 query에 해당하는 사람을 이진탐색으로 찾는 방식으로 품

        2 레벨 맞나.....
        너무 어려움,,

    '''

    answer = [0] * len(query)

    filters = []
    counter = {}

    # 카테고리들
    categorys = [
        ['cpp', 'java', 'python', '-'],
        ['backend', 'frontend', '-'],
        ['junior', 'senior', '-'],
        ['chicken', 'pizza', '-']
    ]

    # 필터(조합) 만들기
    def makeCategoryOfFilters(now_filter, idx):
    
        if idx == len(categorys):
            filters.append(now_filter)
            return

        for category in categorys[idx]:
            makeCategoryOfFilters(now_filter + [category], idx + 1)
    

    makeCategoryOfFilters([], 0)

    # 필터(조건) 에 해당하는 사람들의 점수 넣어두기
    for filter in filters:

        lang, group, career, food = filter

        scores = []
        for person_info in info:
            person_info = list(person_info.split(' '))
            
            if lang != '-' and lang not in person_info:
                continue
            
            if group != '-' and group not in person_info:
                continue

            if career != '-' and career not in person_info:
                continue

            if food != '-' and food not in person_info:
                continue
            
            scores.append(int(person_info[-1]))
        
        # 이진 탐색을 위해 정렬해두기
        scores.sort()
        # 해당 조건에 맞는 사람들의 점수
        counter[''.join(filter)] = scores

    for i, q in enumerate(query):
        lang, group, career, food = q.split(' and ')
        food, score = food.split(' ')
        score = int(score)

        # 이진탐색으로 조건에 해당하는 사람들의 수 계산하기
        filter = ''.join([lang, group, career, food])
        answer[i] = len(counter[filter]) - bisect.bisect_left(counter[filter], score)

    return answer


print(solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"], ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]))


def firstSolu(info, query):

    '''
        다른 사람 풀이
        프로그래머스 다른 사람 풀이
        https://school.programmers.co.kr/learn/courses/30/lessons/72412/solution_groups?language=python3

        나랑 똑같은 방식의 풀이
        재귀랑 라이브러리를 하나도 사용안했다는 점이 다른 점이고

        4중첩 for 문은 정말 신기함 ㅋㅋ

    '''

    data = dict()

    for a in ['cpp', 'java', 'python', '-']:
        for b in ['backend', 'frontend', '-']:
            for c in ['junior', 'senior', '-']:
                for d in ['chicken', 'pizza', '-']:
                    data.setdefault((a, b, c, d), list())
    
    for i in info:
        i = i.split()
        for a in [i[0], '-']:
            for b in [i[1], '-']:
                for c in [[i][2], '-']:
                    for d in [i[3], '-']:
                        data[(a, b, c, d)].append(int(i[4]))
    
    for k in data:
        data[k].sort()

    answer = list()
    for q in query:
        q = q.split()

        pool = data[(q[0], q[2], q[4], q[6])]
        find = int(q[7])

        l = 0
        r = len(pool)
        mid = 0
        while i < r:
            mid = (r + l) // 2
            if pool[mid] >= find:
                r = mid
            else:
                l = mid + 1
        
        answer.append(len(pool) - 1)
    
    return answer