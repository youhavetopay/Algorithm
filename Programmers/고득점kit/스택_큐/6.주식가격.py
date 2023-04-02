def solution(prices):

    '''
        나의 풀이
        주식 가격들이 얼마동안 떨어지지 않는지 체크하는 문제

        스택을 활용하면 그래도 쉽게?? 푸는듯?? ㅋㅋ

        비슷한 문제를 몇번 풀어본 기억이 있어서
        스택을 떠올리는데 크게..?? 어렵지 않은듯 함 ㅋㅋ
    '''

    answer = []

    # 스택에는 [index, price]를 담아둠
    stack = []

    # dict에는 index를 키로 하고 
    # 해당 index의 price가 유지한 시간이 저장됨
    time_table = {}
    
    # 길이 = 최대 유지 시간
    length = len(prices)-1

    # 전체를 순회
    for idx, price in enumerate(prices):
        
        # 스택의 top의 가격보다 작을 때
        # => top의 가격이 떨어졌을 때
        while stack and stack[-1][1] > price:
            # pop하고 idx로 유지한 시간 계산
            top_idx, top_price = stack.pop()
            time_table[top_idx] = idx - top_idx
        
        # 스택에 새로운 가격 추가
        stack.append([idx, price])
    
    # 스택에 남아 있는 시간들 계산
    for idx, price in stack:
        time_table[idx] = length - idx

    # index 순으로 정렬해서 answer에 추가
    for key in sorted(time_table.keys()):
        answer.append(time_table[key])

    return answer


print(solution([2, 5, 7, 1, 2]))

def firstSoul(prices):

    '''
        다른 사람 풀이
        https://velog.io/@soo5717/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EC%A3%BC%EC%8B%9D%EA%B0%80%EA%B2%A9-Python

        나랑 비슷한 풀이인듯 함
        대신 answer에 미리 최대값?? 을 채워두고 시작해서
        굳이 dict을 사용할 필요가 없는듯 해서 훨씬 빠름 -> 정렬이 없어서 ㅋㅋㅋ

        그리고 stack에 price를 같이 넣는게 아니라 
        index만 넣어서 불필요한 값을 줄인듯??

        훨씬 효율적이고 코드도 깔끔한듯 함 ㅋㅋ
    '''

    length = len(prices)
    answer = [i for i in range(length-1, -1, -1)]

    stack = [0]
    for i in range(1, length):
        while stack and prices[stack[-1]] > prices[i]:
            j = stack.pop()
            answer[j] = i - j
        
        stack.append(i)

    return answer