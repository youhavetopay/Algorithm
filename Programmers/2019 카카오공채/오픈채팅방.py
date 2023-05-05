def solution(record):

    '''
        나의 풀이
        채팅방 로그를 구현하는 문제

        나의 접근법
        그냥 문제에서 구현하라는데로 구현함 ㅋㅋ

        예전에 풀었던 문제인데
        예전이랑 풀이가 똑같음 ㅋㅋㅋㅋㅋㅋㅋ
    '''

    answer = []
    
    user_id_by_name = {}
    logs = []

    for log in record:

        info = list(map(str, log.split()))

        if info[0] != 'Leave':
            user_id_by_name[info[1]] = info[2]

        logs.append([info[0], info[1]])


    for method, user_id in logs:
        if method == 'Enter':
            answer.append(user_id_by_name[user_id] + '님이 들어왔습니다.')
        elif method == 'Leave':
            answer.append(user_id_by_name[user_id] + '님이 나갔습니다.')


    return answer

print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))



def firstSolu(record):

    '''
        다른 사람 풀이
        프로그래머스 다른 사람 풀이
        https://school.programmers.co.kr/learn/courses/30/lessons/42888/solution_groups?language=python3

        나랑 똑같은 방식으로 품
        대신 Enter, Leave 메시지를 좀더 깔끔하게 관리한 점??
        예쁜듯 ㅎㅎ

    '''

    answer = []
    namespace = {}
    printer = {'Enter':'님이 들어왔습니다.', 'Leave':'님이 나갔습니다.'}

    for r in record:
        rr = r.split(' ')

        if rr[0] in ['Enter', 'Leave']:
            namespace[rr[1]] = rr[2]
    
    for r in record:
        if r.split(' ')[0] != 'Change':
            answer.append(namespace[r.split(' ')[1]] + printer[r.split(' ')[0]])

    return answer

def secondSolu(record):

    '''
        다른 사람 풀이 2
        프로그래머스 다른 사람 풀이

        원리는 똑같은데
        극한의 숏코딩이라서 가져와봄 ㅋㅋㅋㅋ
        정말 파이써닉하다. ㅋㅋㅋ
    '''

    user_id = {EC.split()[1]:EC.split()[-1] for EC in record if EC.startswith('Enter') or EC.startswith('Change')}
    return [f'{user_id[E_L.split()[1]]}님이 들어왔습니다.' if E_L.startswith('Enter') else f'{user_id[E_L.split()[1]]}님이 나갔습니다.' for E_L in record if not E_L.startswith('Change')]