def solution(sizes):

    '''
        나의 풀이
        눕힐 수 있는 직사각형들을 만족하는 최소 넓이를 구하는 문제

        그냥 차근차근 하나하나 체크하는 방식으로 품

        레벨 1 문제 치곤 좀 어려웠음 ㅋㅋㅋㅋ
        예전에 풀었던 문제임에도 불구하고 오래걸렸음 ㅋㅋㅋ
    '''

    # 최대 너비와 높이
    max_height = sizes[0][0]
    max_width = sizes[0][1]

    # 탐색
    for i in range(1, len(sizes)):
        width, height = sizes[i]

        # 최대 너비와 높이를 만족하거나
        # 눕혔을때 만족하면 넘어감
        if (width <= max_width and height <= max_height) or \
            (height <= max_width and width <= max_height):
            continue
        
        # 눕히지 않은 상태에서 넓이 계산
        temp_max_width = max(width, max_width)
        temp_max_height = max(height, max_height)
        temp_area = temp_max_width * temp_max_height

        # 눕힌 상태에서 넓이 계산
        cross_max_width = max(height, max_width)
        cross_max_height = max(width, max_height)
        cross_area = cross_max_width * cross_max_height

        # 눕히지 않은 넓이가 더 작을 때
        if temp_area < cross_area:
            max_width = temp_max_width
            max_height = temp_max_height
        else:
            max_width = cross_max_width
            max_height = cross_max_height


    return max_height * max_width


def firstSoul(sizes):

    '''
        다른 사람 풀이
        https://velog.io/@guswl8280/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EC%B5%9C%EC%86%8C-%EC%A7%81%EC%82%AC%EA%B0%81%ED%98%95-Python

        너비와 높이를 비교해서
        한쪽에 넣어두고 해당 리스트에서 각각 최대값을 뽑아서 품 ㅋㅋ

        와 역시 코드 깔끔함 ㅋㅋㅋ
        예전에 내가 풀었던....?? 코드도 이러한 풀이였음
        보고 했나? ㅋㅋㅋㅋ
    '''

    w = []
    h = []

    for i in range(len(sizes)):
        if sizes[i][0] >= sizes[i][1]:
            w.append(sizes[i][0])
            h.append(sizes[i][1])
        else:
            h.append(sizes[i][0])
            w.append(sizes[i][1])

    return max(w) * max(h)


def secondSoul(sizes):

    '''
        다른 사람 풀이 2
        https://velog.io/@guswl8280/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EC%B5%9C%EC%86%8C-%EC%A7%81%EC%82%AC%EA%B0%81%ED%98%95-Python

        첫번째 다른 사람 풀이랑 같은 맥락??이지만
        훨씬 파이써닉한 풀이임 ㅋㅋ
        큰값중 최대 값과 최소값중 최대값을 곱해주면 됨... ㄷㄷㄷ
    '''

    return max(max(x) for x in sizes) * max(min(x) for x in sizes)