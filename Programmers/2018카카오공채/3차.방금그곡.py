def convertTime(time):
    h, m = map(int, time.split(':'))

    m += h * 60

    return m

def convertM(m):

    m_list = []
    for w in m:
        if w == '#':
            m_list[-1] += '#'
        else:
            m_list.append(w)
    
    return m_list

def checkSong(m, song_m):

    for i in range(len(song_m) - len(m) + 1):
        if m == song_m[i:i+len(m)]:
            return True
    
    return False


def solution(m, musicinfos):

    '''
        나의 풀이
        악보를 가지고 플레이된 노래들 중에서 일치하는 노래를 찾는 문제

        나의 접근법
        그냥 하라는데로 구현했음 ㅋㅋ

        최근에 프로그래머스 스킬체크 2레벨 에서 푼적 있어서
        문제 안 읽어보고 바로 풀었음 ㅎㅎ
    '''

    answer = '(None)'

    # 악보를 리스트로 만들기
    m_list = convertM(m)
    max_play_time = -1

    for music_info in musicinfos:
    
        start, end, name, song_m = map(str, music_info.split(','))

        # 플레이된 시간 계산하기 -> 분단위로
        start = convertTime(start)
        end = convertTime(end)
        play_time = end - start

        # 해당 노래의 악보를 리스트로 만들고
        # 플레이된 시간에 따라 악보 수정해주기
        song_m = convertM(song_m)
        if len(song_m) < play_time:

            i = 0
            while len(song_m) < play_time:
                song_m.append(song_m[i])
                i += 1
        
        elif len(song_m) > play_time:
            song_m = song_m[:play_time]
        
        # 나의 악보가 해당 노래 악보에 포함되면서
        # 재생시간이 가장 긴 노래를 찾기
        if checkSong(m_list, song_m) and max_play_time < play_time:
            answer = name
            max_play_time = play_time


    return answer



print(solution("ABCDEFG", ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]))


def shap_to_lower(s):
    s = s.replace('C#', 'c').replace('D#', 'd').replace('F#', 'f').replace('G#','g').replace('A#','a')
    return s

def firstSoul(m, musicinfos):

    '''
        다른 사람 풀이
        프로그래머스 다른 사람 풀이
        https://school.programmers.co.kr/learn/courses/30/lessons/17683/solution_groups?language=python3

        전반적으로 나랑 똑같이 했고
        시간을 계산하는 부분이랑 악보를 전처리 하는 부분에 있어서 나랑 좀 다름
        악보를 저렇게 전처리 하는게 좀더 깔끔할수도??
    '''
    
    answer = [0, '(None)']

    m = shap_to_lower(m)

    for info in musicinfos:
        split_info = info.split(',')
        time_length = (int(split_info[1][:2]) - int(split_info[0][:2]))*60 + int(split_info[1][-2:]) - int(split_info[0][-2:])
        title = split_info[2]
        part_notes = shap_to_lower(split_info[-1])

        full_notes = part_notes*(time_length // len(part_notes)) + part_notes[:time_length%len(part_notes)]
        if m in full_notes and time_length > answer[0]:
            answer[time_length, title]
    
    return answer[-1]