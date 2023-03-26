import collections

def solution(participant, completion):

    '''
        나의 풀이
        참가자와 완료자 리스트가 있을때 
        완료자 리스트에 없는 사람을 찾는 문제 (동명이인 있음)

        Counter를 통해 품
        전부 카운트 한 다음
        참가자에서 완료자를 빼주면 완료하지 못한자가 나옴
        
        이것도 예전에 풀었었는데 참 희한하게 푼듯 ㅋㅋㅋㅋ
        Counter를 몰라서 직접 카운팅하고 
        key를 통해 서로를 비교하면서 없거나 일치하지 않으면 정답으로 함
        지금보니까 순서 다르게 입력되면 어쩔려고 이렇게 푼거야... ㅋㅋㅋㅋㅋ
        
        그래도 그때에 비해 성장한거라고 생각하면 살짝 기분 좋음 ㅋㅋㅋㅋ
    '''

    answer = ''

    parti_counter = collections.Counter(participant)
    comple_counter = collections.Counter(completion)

    answer = list((parti_counter - comple_counter).keys())[0]

    return answer

print(solution(["leo", "kiki", "eden"], ["eden", "kiki"]))

def firstSoul(participant, completion):
    
    '''
        다른 사람 풀이
        https://jione-e.tistory.com/44

        둘다 정렬을 해서
        반복문으로 같은 위치에서 서로 다르면 해당 사람이
        완주를 못한 사람이고 
        전부 같다면 마지막 사람이 완주하지 못한사람

        내가 예전풀이에서 지적한 부분?? (순서가 다르게 입력)
        을 반영하면 이렇게 해야 할듯?? ㅋㅋㅋ
    '''


    participant.sort()
    completion.sort()

    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]
    
    return participant[-1]