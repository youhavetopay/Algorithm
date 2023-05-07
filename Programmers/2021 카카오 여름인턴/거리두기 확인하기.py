def checkLength(x, y):

    if 0 <= x < 5 and 0 <= y < 5:
        return True
    
    return False

def checkPartition(now, target, place):

    x, y = now
    t_x, t_y = target

    # 위쪽
    if y > t_y:
        
        if y - 1 == t_y:
            # 대각선 파티션 존재
            if place[t_y][x] == 'X' and place[y][t_x] == 'X':
                return True
            
        
        # 2칸 위에 사람 있고 중간에 파티션 있을 때
        if y - 2 == t_y and place[y - 1][x] == 'X':
            return True
        

    elif y == t_y:
        
        if x + 2 == t_x and place[y][x + 1] == 'X':
            return True
        
        if x - 2 == t_x and place[y][x - 1] == 'X':
            return True
        

    else:

        if y + 1 == t_y:
            # 대각선 파티션 존재
            if place[t_y][x] == 'X' and place[y][t_x] == 'X':
                return True
            
        
        # 2칸 아래에 사람 있고 중간에 파티션 있을 때
        if y + 2 == t_y and place[y + 1][x] == 'X':
            return True
        
    
    return False


def checkDistance(x, y, place):

    # 사람을 찾은 위치에서
    # 맨해튼 거리 2 이하인 모든 지점을 탐색
    # 사람이 있으면 파티션 유무 체크하기
    vectors = [
        [0, -2], 
        [-1, -1], [0, -1], [1, -1],
        [-2, 0], [-1, 0], [1, 0], [2, 0],
        [-1, 1], [0, 1], [1, 1],
        [0, 2],
    ]

    for dx, dy in vectors:
        check_x, check_y = x + dx, y + dy

        if checkLength(check_x, check_y) and \
            place[check_y][check_x] == 'P':

            if not checkPartition([x, y], [check_x, check_y], place):
                return False
    
    return True

    

def solution(places):

    '''
        나의 풀이
        맨해튼 거리 2 이하일 때 거리두기가 되는지 체크하는 문제

        나의 접근법
        사람이 있으면 해당 좌표에서 맨해튼 거리 2 까지 모든 지점을
        체크하는 방식으로 품

        예전에도 이런 방식으로 풀었던 것 같은데
        이게 중복 검사를 많이 하긴 하지만 
        그냥 이해하기도 편하고 간단한 방법인듯?? ㅋㅋㅋㅋㅋ
    '''

    answer = []

    for place in places:

        check = False

        # 사람 찾기
        for y, line in enumerate(place):
            for x, loc in enumerate(line):
                if loc == 'P':
                    if not checkDistance(x, y, place):
                        check = True

                if check:
                    break
            
            if check:
                break
        
        if check:
            answer.append(0)
        else:
            answer.append(1)

    return answer


def check(place):

    for irow, row in enumerate(place):
        for icol, cell in enumerate(row):
            if cell != 'P':
                continue

            if irow != 4 and place[irow + 1][icol] == 'P':
                return 0
            
            if irow < 3 and place[irow + 2][icol] == 'P' and place[irow + 1][icol] != 'X':
                return 0
            
            if irow < 3 and place[irow][icol + 2] == 'P' and place[irow][icol + 1] != 'X':
                return 0
            
            if irow != 4 and icol != 4 and place[irow + 1][icol + 1] == 'P' and (place[irow + 1][icol] != 'X' or place[irow][icol + 1] != 'X'):
                return 0
            
            if irow != 4 and icol != 0 and place[irow + 1][icol - 1] == 'P' and (place[irow + 1][icol] != 'X' or place[irow][icol - 1] != 'X'):
                return 0
            
    return 1

def firstSolu(places):

    '''
        다른 사람 풀이
        프로그래머스 다른 사람 풀이

        이분도 그냥 전부 체크하는 방식으로 푸심 ㅋㅋㅋ
    '''

    return [check(place) for place in places]