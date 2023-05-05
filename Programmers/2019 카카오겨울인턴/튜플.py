def solution(s):

    '''
        나의 풀이
        문자열로된 튜플 모음이 주어지면
        순서에 따른 최종 튜플?? 을 구하는 문제

        나의 접근법
        해당 튜플의 파싱을 하고 길이를 기준으로 넣어둠
        그 다음 길이 순으로 정렬해서 answer에 없는 숫자를 
        차례대로 넣어주는 방식으로 품

        최종 튜플?의 길이가 10만 이하라고 하길래
        set을 사용해서 중복여부를 체크할려고 했는데
        안해도 통과해서 신기했음 ㅋㅋ
        그래도 하니까 시간복잡도 확 줄어듬 ㅋㅋ
    '''

    answer = []
    find_tuple = set()

    length_by_tuple = {}

    # 양쪽 끝의 { } 지워주기
    s = s[1:-1]

    # 한 튜플을 모아둘 문자열
    words = ''

    # 덩어리 체크용 ㅋㅋ
    flag = False

    for word in s:
        # { 이거는 덩어리 시작이니 넣어주기
        if word == '{':
            flag = True

        # } 이거면 덩어리가 끝난거니까 파싱해서 길이별로 넣어두기
        elif word == '}':
            nums = list(map(int, words[1:].split(',')))
            length_by_tuple[len(nums)] = nums
            words = ''
            flag = False

        if flag:
            words += word

    # 길이 순으로 정렬해서 하나씩 넣어줌
    for length in sorted(length_by_tuple.keys()):
        for num in length_by_tuple[length]:
            if num not in find_tuple:
                answer.append(num)
                find_tuple.add(num)
                break

    return answer

print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))


import re
import collections

def firstSolu(s):

    '''
        다른 사람 풀이
        프로그래머스 다른 사람 풀이

        ㅋㅋㅋㅋㅋ
        정규식에 Counter 까지 사용해서 두줄로 줄임 ㅋㅋㅋㅋ
        
        정규식으로 추려내고
        숫자의 빈도를 카운팅
        숫자 빈도가 높은게 먼저 있는 숫자.. ㄷㄷㄷㄷ
    '''

    s = collections.Counter(re.findall('\d+', s))
    return list(map(int, [k for k, v in sorted(s.items(), key=lambda x: x[1], reverse=True)]))

print(firstSolu("{{2},{2,1},{2,1,3},{2,1,3,4}}"))