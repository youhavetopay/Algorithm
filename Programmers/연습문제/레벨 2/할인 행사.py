from collections import defaultdict, Counter

def solution(want, number, discount):

    '''
        나의 풀이
        차례대로 해당 물건을 할인하는 리스트가 주어질때
        해당 일부터 10일간 내가 구매하려는 모든 물건을 할인할때 회원가입을 하는데
        회원가입이 가능한 날짜의 개수를 구하는 문제

        나의 접근법
        투포인터로 defaultdict에 10일간의 물건 할인 정보를 담아두고
        내가 구매하려는 물건이 모두 할인하고 있으면 회원가입이 가능한 날이므로 answer에 1을 더해줌



        문제 이해를 못해서 살짝 어려웠음 ㅋㅋㅋㅋ
        회원가입을 하는 최소의 날을 계산해서 왜맞틀? 하면서 고민함 ㅋㅋㅋ
    '''

    answer = 0

    # 내가 구매해야하는 물건 카운팅
    need_product = {}
    for name, count in zip(want, number):
        need_product[name] = count

    discount_product = defaultdict(int)
    
    # 할인정보가 최소 10이라서 첫 10일 할인정보 카운팅
    for i in range(9):
        discount_product[discount[i]] += 1
    
    # 넣고 빼면서 체크
    left = 0
    for right in range(9, len(discount)):

        discount_product[discount[right]] += 1
        print(discount_product)
        if check_can_signup(need_product, discount_product):
            answer += 1
        
        discount_product[discount[left]] -= 1
        if discount_product[discount[left]] == 0:
            del discount_product[discount[left]]
        
        left += 1



    return answer


def check_can_signup(my, discount):

    for my_product in my:
        if my[my_product] > discount[my_product]:
            return False
        
    return True


print(solution(	["apple"], [10], ["banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana"]))

def firstSolu(want, number, discount):

    '''
        다른 사람 풀이
        프로그래머스 다른 사람 풀이
        https://school.programmers.co.kr/learn/courses/30/lessons/131127/solution_groups?language=python3

        Counter로 discount를 10개 만큼 슬라이스 해서 품
        이게 되나???
        내가 구매하려는 물건의 개수가 10개보다 작으면
        Counter 한거랑 값이 달라서 안되는거 아닌가?? 뭐지??

        아 ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ
        지금 보니까 number의 합이 무조건 10이네 ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ
    '''

    answer = 0
    dic = {}
    for i in range(len(want)):
        dic[want[i]] = number[i]

    for i in range(len(discount) - 9):
        if dic == Counter(discount[i:i+10]):
            answer += 1
    
    return answer


temp = ["apple"] * 10
print({"apple" : 5} == Counter(temp))