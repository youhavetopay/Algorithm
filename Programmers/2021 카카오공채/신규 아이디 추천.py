def checkWord(word: str):

    if word.isalpha():
        return True
    
    if word.isnumeric():
        return True
    
    if word in ['-', '.', '_']:
        return True
    
    return False

def solution(new_id: str):

    '''
        나의 풀이
        정해진 규칙에 따라 문자열을 수정하는 문제

        나의 접근법
        진짜 구현하라는데로 똑같이 구현함 ㅋㅋㅋ

        파이썬이 참 알고리즘 풀기 좋은듯 ㅋㅋㅋ
    '''

    now_id = new_id

    now_id = now_id.lower()

    i = 0

    temp_id = list(now_id)
    while i < len(temp_id):
        if not checkWord(temp_id[i]):
            temp_id.pop(i)
            continue
        
        i += 1

    now_id = ''.join(temp_id)

    while '..' in now_id:
        now_id = now_id.replace('..', '.')

    if now_id and now_id[0] == '.':
        now_id = now_id[1:]
    if now_id and now_id[-1] == '.':
        now_id = now_id[:-1]

    if now_id == '':
        now_id += 'a'

    if len(now_id) >= 16:
        now_id = now_id[:15]
    
    if now_id and now_id[-1] == '.':
        now_id = now_id[:-1]

    while len(now_id) <= 2:
        now_id += now_id[-1]

    return now_id

print(solution("...!@BaT#*..y.abcdefghijklm"))


import re

def firstSolu(new_id):

    '''
        다른 사람 풀이
        프로그래머스 다른 사람 풀이

        역시.. 정규식을 사용하니 짧게 풀수 있는듯..
        정규식 배워야하는데 엄두가 안남.ㅋㅋㅋㅋ
    '''

    st = new_id
    st = st.lower()
    st = re.sub('[^a-z0-9\-_.]', '', st)
    st = re.sub('\.+', '.', st)
    st = re.sub('^[.]|[.]$', '', st)
    st = 'a' if len(st) == 0 else st[:15]
    st = re.sub('^[.]|[.]$', '', st)
    st = st if len(st) > 2 else st + ''.join(st[-1] for i in range(3 - len(st)))

    return st