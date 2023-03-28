import collections


def solution(clothes):

    '''
        나의 풀이(못품 ㅠㅠ 시간초과..)
        옷이 주어지면 모든 옷 조합을 구하는 문제

        일단 나의 접근법은
        그냥 모든 조합을 구하는 것으로 접근했었음 ㅋㅋ
        근데 1번테스트케이스가 시간초과로 통과를 못함 ㅋㅋ

        에전에 풀었던?? 문제인데 못품 ㅋㅋㅋ
        보니까 이전에 백준에서 한번 풀어본 기록이 있는데 
        기억 1도 안남 ㅋㅋㅋㅋㅋㅋㅋㅋㅋ
    '''
    
    answer = len(clothes)

    clothe_types = collections.defaultdict(int)

    for name, type in clothes:
        clothe_types[type] += 1

    types = list(clothe_types.keys())

    def dfs(max_select_count, last_select_idx, seleted_count, day):

        total_day = 0

        # 다 골랐으면 반환
        if max_select_count == seleted_count:
            return day

        # 하나씩 선택
        for i in range(last_select_idx, len(types)):
            total_day += dfs(max_select_count, i+1, seleted_count + 1, day * clothe_types[types[i]])
            
        return total_day
    
    # 최소 2개부터 최대 선택할 수 있는 종류까지
    for i in range(2, len(clothe_types.keys())+1):
        answer += dfs(i, 0, 0, 1)

    return answer

print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))


def firstSoul(clothes):

    '''
        이전에 내가 풀었던 풀이 ㅋㅋㅋㅋ
        일단 종류별로 카운팅 한 다음

        종류의 개수의 +1 하고 계속 곱하고
        마지막에 -1 해주면 풀림.....

        모든 경우의 수를 구하면
        아무것도 안 입은 경우도 나오기 때문에
        -1을 해줘야함

        그리고 곱할때도
        각 옷 종류를 입지 않는 경우도 있기 때문에
        1 더해줘야 함..
    '''

    myCloth = {}
    answer = 0
    for tempList in clothes:
        try:
            myCloth[tempList[1]] += 1
        
        except KeyError:
            myCloth[tempList[1]] = 1

    coll = 1
    for key, value in myCloth.items():
        coll *= value + 1
    
   
    answer = coll - 1
    return answer