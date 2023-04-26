def getLocationXY(num):

    x, y = 0, 0

    board = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
        ['*', 0, '#']
    ]

    for i, line in enumerate(board):
        if num in line:
            y = i
            x = line.index(num)
            return [x+1, y+1]
        
def calDist(now_num, next_num):

    # 값을 통해 해당 위치 가져옴
    now_x, now_y = getLocationXY(now_num)
    next_x, next_y = getLocationXY(next_num)

    # 대각선 이동은 불가능해서 그냥 거리차이를 계산
    # (두 점 사이의 거리하니까 통과 못함 ㅋㅋ)
    dist = abs(now_x - next_x) + abs(now_y - next_y)
    return dist


def solution(numbers, hand):

    '''
        나의 풀이
        키패드를 누르는 손을 출력하는 문제

        나의 접근법
        키패드를 2차원 리스트로 만들어서
        해당 좌표끼리의 거리차이를 구해서 비교하는 방식으로 품

        예전에 풀었던 문제이지만
        내가 태어나서 처음 본 코딩테스트 문제라서 ㅋㅋㅋ
        풀때마다 살짝 긴장됨 ㅋㅋㅋ
    '''

    answer = ''

    # 처음 위치 저장
    L_hand = '*'
    R_hand = '#'

    for num in numbers:
        # 왼손 인 경우
        if num in [1, 4, 7]:
            answer += 'L'
            L_hand = num

        # 오른손인 경우
        elif num in [3, 6, 9]:
            answer += 'R'
            R_hand = num

        else:
            # 거리를 계산 후 비교
            L_dist = calDist(L_hand, num)
            R_dist = calDist(R_hand, num)

            print(L_dist, R_dist)

            if L_dist < R_dist:
                answer += 'L'
                L_hand = num
            elif L_dist > R_dist:
                answer += 'R'
                R_hand = num
            else:
                # 거리가 같을 땐 왼손잡이 인지 오른손잡이 인지 체크 후 더해줌
                if hand == 'right':
                    answer += 'R'
                    R_hand = num
                else:
                    answer += 'L'
                    L_hand = num


    return answer


def firstSolu(numbers, hand):

    '''
        다른 사람 풀이
        프로그래머스 다른 사람 풀이

        나랑 접근법이 똑같음
        키패드를 좌표로 나타내고 하는 것..
        대신 좌표값을 dict 형식으로 이미 넣어둠
        그래서 훨씬 빠를듯?? 거의 차이는 안나겠지만 ㅋㅋ
    '''

    answer = ''
    key_dict = {1:(0,0),2:(0,1),3:(0,2),
                4:(1,0),5:(1,1),6:(1,2),
                7:(2,0),8:(2,1),9:(2,2),
                '*':(3,0),0:(3,1),'#':(3,2)}
    
    left = [1, 4, 7]
    right = [3, 6, 9]

    lhand = '*'
    rhand = '#'

    for i in numbers:
        if i in left:
            answer += 'L'
            lhand = i
        elif i in right:
            answer += 'R'
            rhand = i
        else:
            curPos = key_dict[i]
            lPos = key_dict[lhand]
            rPos = key_dict[rhand]

            ldist = abs(curPos[0] - lPos[0]) + abs(curPos[1] - lPos[1])
            rdist = abs(curPos[0] - rPos[0]) + abs(curPos[1] - rPos[1])

            if ldist < rdist:
                answer += 'L'
                lhand = i
            elif ldist > rdist:
                answer += 'R'
                rhand = i
            else:
                if hand == 'left':
                    answer += 'L'
                    lhand = i
                else:
                    answer += 'R'
                    rhand = i

    return answer