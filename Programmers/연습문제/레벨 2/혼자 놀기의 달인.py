def solution(cards):

    '''
        나의 풀이
        처음에 상자를 DFS 형식으로 열고
        나머지 상자를 DFS로 방식으로 열었을때
        처음 DFS의 결과값이랑 두번째 DFS의 결과값의 곱의 
        최대값을 계산하는 문제

        나의 접근법
        상자 수가 최대 100개이고 DFS도 최대 두번만 하기 때문에
        그냥 완전탐색으로 풀었음
        첫번째를 선택하고 DFS로 한번 다 열고
        나머지 안 열어둔 것도 차례대로 선택해보면서 최대값을 계산함

        설명이 좀 길어서 그렇지 그렇게 어려운 문제는 아닌듯??
    '''

    answer = 0

    # 박스의 상태값을 저장(열었는지 안열었는지)
    box_state = init_card_open(cards)

    # 박스를 몇번 연속으로 여는지 체크
    def open_box(next_box, now_count):
        count = 0

        if box_state[next_box] == False:
            box_state[next_box] = True
            count = open_box(cards[next_box-1], now_count + 1)
        else:
            return now_count
        
        return count

    # 첫번째로 선택한 상자
    for num in cards:
        first_group = open_box(num, 0)

        # 두번째로 선택한 상자
        second_group = 0
        for num in cards:
            if box_state[num] == False:
                second_group = max(second_group, open_box(num, 0))
        
        answer = max(answer, first_group * second_group)

        # 박스 상태 초기화
        box_state = init_card_open(cards)


    return answer

def init_card_open(cards):

    check_open = {}

    for card in cards:
        check_open[card] = False

    return check_open

print(solution([8,6,3,7,2,5,1,4]))


def firstSolu(cards):

    '''
        다른 사람 풀이
        프로그래머스 다른 사람 풀이
        https://school.programmers.co.kr/learn/courses/30/lessons/131130/solution_groups?language=python3

        열었던 박스를 계속 리스트에 담고
        해당 리스트를 정렬해서 중복되지 않게 answer에 넣고
        마지막에는 answer를 길이를 기준으로 정렬해서
        제일 긴거 두개를 곱해주는 방식으로 계산함 ㄷㄷㄷ
        
    '''

    answer = []
    
    for i in range(len(cards)):
        tmp = []
        
        while cards[i] not in tmp:
            tmp.append(cards[i])
            i = cards[i] - 1
        
        answer.append([] if sorted(tmp) in answer else sorted(tmp))
    
    answer.sort(key=len)

    return len(answer[-1] * len(answer[-2]))