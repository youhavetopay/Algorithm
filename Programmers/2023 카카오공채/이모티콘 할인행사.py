def solution(users, emoticons):

    '''
        나의 풀이
        이모티콘 플러스 가입자를 최대로 늘리는
        이모티콘 할인율을 찾아서 가입자 수와 판매 금액을 계산하는 문제

        나의 접근법
        이모티콘 종류가 7개까지고 할인율의 종류도 4개라서
        그냥 모든 할인율 조합을 구해서 계산하는 방식으로 품
        완전탐색?? 정도 ㅋㅋㅋ

        문제 난이도도 조합만 잘 찾고 구현사항대로만 구현하면
        그렇게 어려운 문제는 아닌듯
        그도 그럴것이지 점수도 1점밖에 안줌 ㅋㅋ
    '''

    answer = [0, 0]

    discount_pers = [10, 20, 30, 40]

    total_pers = []

    # 모든 할인율 조합 구하기
    def dfs(now_pers, i):

        if i == len(emoticons):
            total_pers.append(now_pers)
            return
        
        for per in discount_pers:
            dfs(now_pers + [per], i+1)
    
    dfs([], 0)

    # 할인율에 따른 가입자와 판매금액 계산하기
    for now_per_idx in range(len(total_pers)):

        plus_count = 0
        money = 0

        for my_buy_per, my_max_money in users:
            
            my_money = 0
            for per, price in zip(total_pers[now_per_idx], emoticons):
                discount_price = price - int((price / 10) * (per // 10))
                if my_buy_per <= per:
                    my_money += discount_price
            
            if my_money < my_max_money:
                money += my_money
            else:
                plus_count += 1
        
        if plus_count > answer[0]:
            answer = [plus_count, money]
        elif plus_count == answer[0] and money > answer[1]:
            answer = [plus_count, money]

    return answer

print(solution([[40, 10000], [25, 10000]], [7000, 9000]))


from itertools import product

def firstSolu(users, emoticons):

    '''
        다른 사람 풀이
        프로그래머스 다른 사람 풀이
        https://school.programmers.co.kr/learn/courses/30/lessons/150368/solution_groups?language=python3

        ㅋㅋㅋㅋㅋ 나랑 풀이법이 완~~~~~~~전 똑같음 ㅋㅋ
        차이점이라면 조합일 라이브러리로 구한것??
        나도 이거 사용해보면 좋을듯?? ㅋㅋㅋ
    '''

    E = len(emoticons)
    result = [0, 0]
    percents = (10, 20, 30, 40)
    prod = product(percents, repeat=E)

    for p in prod:
        prod_members, prod_price = 0, 0
        for buy_percent, max_price in users:
            user_price = 0
            for item_price, item_percent in zip(emoticons, p):
                if item_percent >= buy_percent:
                    user_price += item_price * (100 - item_percent) * 0.01
            
            if user_price >= max_price:
                prod_members += 1
            else:
                prod_price += user_price
        
        result = max(result, [prod_members, prod_price])
    
    return result
                