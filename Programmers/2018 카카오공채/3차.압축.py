def solution(msg):

    '''
        나의 풀이
        문자를 인덱싱?? 하는 문제??
        그냥 문제 따라서 구현만 잘하면 되는 문제

        문제 자체는 어렵지 않음
        근데 슬라이싱을 잘못해서 좀 오래걸림. ㅋㅋㅋ
    '''

    answer = []

    # 알파벳 인덱스 넣어주기
    database = {}
    for i in range(1, 27):
        database[chr(64+i)] = i

    max_index = 26
    
    i = 0
    while i < len(msg):

        j = 1
        
        # 해당 문자가 색인이 되어있다면 인덱스 올리기
        while i+j <= len(msg) and msg[i:i+j] in database:
            j += 1

        # 마지막 문자의 색인 번호 넣어주기
        answer.append(database[msg[i:i+j-1]])

        # 최대 인덱스 높여주고 인덱싱 안된 문자 해주기
        max_index += 1
        database[msg[i:i+j]] = max_index
        
        # 인덱싱 안된 문자의 순서부터 시작
        i = i+j-1


    return answer

print(solution('TOBEORNOTTOBEORTOBEORNOT'))




def firstSoul(msg):

    '''
        다른 사람 풀이
        프로그래머스 다른 사람 풀이
        https://school.programmers.co.kr/learn/courses/30/lessons/17684/solution_groups?language=python3

        코드 디게 깔끔하게 구현하신듯?? ㅋㅋㅋ
    '''

    # 알파벳 인덱싱 해주기
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    d = {k : v for (k, v) in zip(alphabet, list(range(1, 27)))}

    answer = []

    while True:
        # 현재 문자가 인덱싱이 되어 있다면 넣어주고 끝내기
        if msg in d:
            answer.append(d[msg])
            break
        
        for i in range(1, len(msg) + 1):
            # 인덱싱 인되어 있다면
            if msg[0:i] not in d:
                # 이전 단어의 인덱싱 넣어주기
                answer.append(d[msg[0:i-1]])
                # 현재 문자 인덱싱 해주기
                d[msg[0:i]] = len(d) + 1
                # 인덱싱 되어 있던 문자 버리기
                msg = msg[i-1:]
                break
    
    return answer