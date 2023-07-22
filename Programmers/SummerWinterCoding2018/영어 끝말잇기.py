
'''
    프로그래머스 영어 끝말잇기
    끝말잇기를 할때 탈락하는 사람과 해당 라운드를 반환하는 문제
'''


def solution(n, words):

    '''
        나의 풀이

        나의 접근법
        처음에 말해야하는 단어 순서를 자신이 알아서 해야하는줄 알았는데
        그게 아니라 말하는 단어 순서가 다 정해져 있어서 문제가 엄~~~~청 쉬워짐

        단어수도 최대 100개까지라서
        그냥 중복검사랑 끝말 잇기가 되고 있는지 확인하면서
        체크하면 됨

        처음에 너무 겁먹은듯 ㅋㅋㅋ
    '''

    answer = [0, 0]

    speak_words = {words[0]:1}
    
    now_turn_player = 2
    now_round = 1

    for i in range(1, len(words)):

        if words[i][0] != words[i-1][-1]:
            return [now_turn_player, now_round]
        
        if words[i] in speak_words:
            return [now_turn_player, now_round]
        
        now_turn_player += 1
        speak_words[words[i]] = 1

        if now_turn_player > n:
            now_turn_player = 1
            now_round += 1


    return answer


def firstSolu(n, words):

    '''
        다른 사람 풀이
        프로그래머스 다른 사람 풀이
        https://school.programmers.co.kr/learn/courses/30/lessons/12981/solution_groups?language=python3

        ㅋㅋㅋ 엄청난 숏코딩 ㅋㅋㅋ
        라운드 순서랑 현재 말하는 사람의 번호는
        나머지 연산을 통해 아주 깔끔히 풀어내심 ㅋㅋ
    '''

    for p in range(1, len(words)):
        if words[p][0] != words[p-1][-1] or words[p] in words[:p]: return [(p%n) + 1, (p//n)+ 1]
    else:
        return [0, 0]