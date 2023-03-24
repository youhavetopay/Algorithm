def solution(array, commands):

    '''
        나의 풀이
        숫자리스트에서 일정구간을 정렬한다음 N번째 숫자를 찾는 문제

        예전에 풀었던 문제였는데
        한번 다시 풀어봄 ㅋㅋ
        근데 풀이가 똑같음 ㅋㅋㅋㅋㅋㅋㅋㅋ
    '''

    answer = []

    for command in commands:
        start, end, idx = command
        print(array[start-1:end])
        answer.append(sorted(array[start-1:end])[idx-1])

    return answer


def firstSoul(array, commands):
    '''
        다른 사람 풀이
        https://datahub.tistory.com/10

        map과 lambda를 사용해서 한줄로 표현함 ㅋㅋㅋ
    '''

    return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))