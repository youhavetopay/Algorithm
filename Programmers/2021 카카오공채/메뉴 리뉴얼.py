import itertools
import collections

def solution(orders, course):

    '''
        나의 풀이
        사람들이 가장 많이 시킨 메뉴의 조합들을 구하는 문제

        나의 접근법 (핵심 풀이를 보고 품..ㅜㅜ)
        combinations으로 모든 경우의 수를 구해서 푸는 방법으로
        했다가 시간초과가 떠서 고민좀 함

        결국 질문하기를 통해서 힌트를 얻었는데
        모든 알파벳의 경우의 수는 5백만개라서 시간초과가 뜨니
        경우의 수를 줄이는게 중요하다고 함

        그래서 애초에 주문 개수가 최소 2개 이상은 되야 한다고 했기에
        사람들의 주문 조합들의 합집합으로만 하면 중복 횟수를 굉장히 줄일수 있다고 함

        그래서 최소 길이를 만족하는 주문들의 조합들의 합집합으로 계산하면
        풀림


        지금까지 레벨 2는 비교적 쉽게 풀었는데 생각보다 어려웠음...
        예외케이스나 극단적인 케이스를 생각하면서 푸는 방법이 좋을 듯 함

    '''

    answer = []

    guest_order = {}

    order_counts = collections.defaultdict(int)

    # 사람 별 주문 메뉴랑 주문 개수 저장해두기
    for i, order in enumerate(orders):
        guest_order[i] = set(list(order))
        order_counts[len(order)] += 1

    for course_count in course:

        # 만들려는 코스 메뉴의 음식 개수가 최소 주문 수보다 작으면 
        # 계산하지 말기
        total_order_count_guest = 0
        for key in order_counts.keys():
            if key >= course_count:
                total_order_count_guest += order_counts[key]
        
        if total_order_count_guest < 2:
            continue

        max_course = []
        max_course_count = 2
        now_combinations = set()

        # 주문들의 조합의 합집합 구하기
        for order in orders:
            if len(order) >= course_count:
                now_combinations = now_combinations | set(itertools.combinations(order, course_count))

        # 몇명이 주문 했는지 체크하기
        for combi in now_combinations:
            now_count = 0
            for values in guest_order.values():
                for now_course in combi:
                    if now_course not in values:
                        break
                else:
                    now_count += 1
            
            if now_count > max_course_count:
                max_course_count = now_count
                max_course = [''.join(sorted(combi))]
            elif now_count == max_course_count:
                max_course.append(''.join(sorted(combi)))
            
        # 두명 이상 주문 했다면 넣어주기
        if max_course_count >= 2 and max_course:
            answer.extend(max_course)

    return sorted(set(answer))


print(solution(["XYZ", "XWY", "WXA"], [2,3,4]))


def firstSolu(orders, course):

    '''
        다른 사람 풀이
        프로그래머스 다른 사람 풀이
        https://school.programmers.co.kr/learn/courses/30/lessons/72411/solution_groups?language=python3

        Counter를 활용해서 엄청 깔끔하게 풀어내심.. ㄷㄷ
        처음에 나도 Counter를 생각했긴 했었는데 이렇게 활용할 방법을 생각을 못해서
        사용을 안했는데..대박 ㅋㅋ

        정말 파이써닉 함..ㅋㅋㅋㅋㅋㅋㅋㅋㅋ
    '''

    result = []

    for course_size in course:
        order_combinations = []

        # 주문 조합 만들기
        for order in orders:
            order_combinations += itertools.combinations(sorted(order), course_size)

        # Counter로 중복 개수를 세고 가장 빈도가 많은 애들 들고 와서 넣어주기
        most_orderd = collections.Counter(order_combinations).most_common()
        result += [ k for k, v in most_orderd if v > 1 and v == most_orderd[0][1] ]


    return [''.join(v) for v in sorted(result)]

print(firstSolu(["XYZ", "XWY", "WXA"], [2,3,4]))