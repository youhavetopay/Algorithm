from collections import defaultdict

def solution(survey, choices):
  
    '''
        나의 풀이
        성격 유형 검사 결과에 따른 성격 유형을 찾아내는 문제
        
        나의 접근법
        문제 엄청 쉬움.. 이해하는데 좀 시간이 걸려서 그렇지
        문제 자체는 엄청 쉬웠음..
        dict 자료형으로 각각의 성격 유형별 점수를 카운팅 해주고
        유형에 따라 높은 얘들을 우선으로 넣어주면 끝
        
        노트북을 오늘 두고 와서 그냥 가볍게
        쉬운 문제로 품.. ㅠㅠ
        다음 부터는 어디 갈때 노트북 들고 다니자...ㅠㅠ
    '''
    answer = ''
    
    mbti_orders = [
        ['R', 'T'],
        ['C', 'F'],
        ['J', 'M'],
        ['A', 'N']
    ]
    
    score_table = defaultdict(int)
    
    for per, score in zip(survey, choices):
        a_per, b_per = per[0], per[1]
        
        if score <= 3:
            score_table[a_per] += 4 - score
        elif score >= 5:
            score_table[b_per] += score - 4
    
    for a_per, b_per in mbti_orders:
        if score_table[a_per] >= score_table[b_per]:
            answer += a_per
        else:
            answer += b_per
    
    return answer
 

def firstSolu(survey, choices):
    
    '''
        다른 사람 풀이
        프로그래머스 다른 사람 풀이
        https://school.programmers.co.kr/learn/courses/30/lessons/118666/solution_groups?language=python3
        
        카운팅을 정말 희한하게 하신듯?? ㅋㅋ
    '''
    
    my_dict = {'RT':0, 'CF':0, 'JM':0, 'AN':0}
    for A, B in zip(survey, choices):
        if A not in my_dict.keys():
            A = A[::-1]
            my_dict[A] -= B - 4
        else:
            my_dict[A] += B - 4
    
    result = ''
    for name in my_dict.keys():
        if my_dict[name] > 0:
            result += name[1]
        elif my_dict[name] < 0:
            result += name[0]
        else:
            result += sorted(name)[0]
    
    return result
