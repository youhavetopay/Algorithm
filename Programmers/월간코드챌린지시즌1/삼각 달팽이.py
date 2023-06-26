def solution(n):

    '''
        나의 풀이
        피라미드 형태로 겉에서 부터 1씩 증가하는 숫자 리스트를
        1차원 리스트로 만드는 문제 (자세한건 문제 참고 ㅋㅋ)

        나의 접근법
        해당 피라미드 형태의 리스트를 구현해서 1차원 리스트로 만들었음

        규칙이 있는것 같은데 
        난 이 정도가 최선인듯 ㅋㅋㅋ
    '''

    # 피라미드 초기화
    # 0번row은 1개 1번은 2개 2번은 3개 .... 이런식
    answer = [ [0] * (i+1) for i in range(n)]

    # 시작 숫자
    now = 1

    while True:
        # 시작할 위치 찾기
        start_row, start_idx = get_start_row_idx(answer)
        
        # 다 채웠으면 끝내기
        if start_row == -1 or start_idx == -1:
            break
        
        # 처음 시작할 층
        top_row_idx = start_row
        
        # 위에서 시작해서 아래로 내려가는데
        # 왼쪽부터 채우기 (0 으로 비워진 곳 까지 채우기)
        while top_row_idx < len(answer) and answer[top_row_idx][start_idx] == 0:
            answer[top_row_idx][start_idx] = now
            top_row_idx += 1
            now += 1
        
        # 맨 밑에 층에 도달하면
        # 해당 층 왼쪽에서 오른쪽 끝까지 채우기 (0으로 비워진 곳 까지 채우기)
        bottom_idx = start_idx + 1
        bottom = answer[top_row_idx - 1]
        while bottom_idx < len(bottom) and bottom[bottom_idx] == 0:
            bottom[bottom_idx] = now
            now += 1
            bottom_idx += 1

        # 다시 시작층까지 올라가면서 채우기
        up_idx = bottom_idx - 2
        for i in range(top_row_idx - 2, start_row, -1):
            answer[i][up_idx] = now
            up_idx -= 1
            now += 1

    # 1차원 리스트로 변환
    new_arr = []
    for floor in answer:
        for num in floor:
            new_arr.append(num)

    return new_arr

def get_start_row_idx(answer):
    start_row, start_idx = -1, -1
    for row, line in enumerate(answer):
        if 0 in line:
            start_row = row
            start_idx = line.index(0)
            return [start_row, start_idx]
    
    return [start_row, start_idx]

print(solution(1000))


def firstSolu(n):

    '''
        다른 사람 풀이
        프로그래머스 다른 사람 풀이
        https://school.programmers.co.kr/learn/courses/30/lessons/68645/solution_groups?language=python3

        나랑 비슷하게
        달팽이? 수열을 만들고 해당 리스트를 sum() 으로 합쳐준듯?
        대신 ny 랑 nx 으로 이동 방향을 정해주면서 아주 깔끔하게 풀어냄 ㅋㅋ
    '''

    # 이동 방향
    # 0 : 아래, 1 : 오른쪽, 2 : 위(오른쪽 끝에서)
    dx = [0, 1, -1]
    dy = [1, 0, -1]
    
    # 초기 리스트
    b = [[0] * i for i in range(1, n+1)]
    
    # 현재 위치
    x, y = 0, 0
    
    # 시작 번호
    num = 1
    # 이동방향의 인덱스 정도?
    d = 0

    # 다 채울때 까지 -> 최대 수가 저거인듯??
    while num <= (n + 1) * n // 2:

        # 한칸 채우기
        b[y][x] = num

        # 다음칸으로 이동
        ny = y + dy[d]
        nx = x + dx[d]
        
        num += 1

        # 리스트 길이를 넘지 않고 아직 채우지 않은 곳일 때
        if 0 <= ny < n and 0 <= nx <= ny and b[ny][nx] == 0:
            y, x = ny, nx
        else:
            # 다른 방향으로 이동하기
            d = (d + 1) % 3
            y += dy[d]
            x += dx[d]
    
    # 완성된 리스트 1차원으로 바꿔주기??  ㄷㄷㄷ
    return sum(b, [])