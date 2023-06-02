def get_dist(start, end):

    start_x, start_y = start
    end_x, end_y = end

    return (((start_x - end_x) ** 2) + ((start_y - end_y) ** 2)) ** (1/2)


def solution(m, n, startX, startY, balls):

    '''
        나의 풀이(못품..진짜 수학 너무 부족한듯..)
        당구에서 원쿠션으로 목표 공을 치는 최소 이동 거리를 계산하는 문제

        나의 접근법
        시작 공이랑 목표공이랑 같은 선에 있으면 ex) x좌표가 같다던가 y가 같다던가
        이등변 삼각형 만들수 있으니 
        두가지 방향으로 쳤을때랑 가까운 벽에 바로 갔다가 오는 거리를 비교해서
        계산했는데
        이러한 경우가 아니라면 어떻게 해야할지 감도 못잡았음...

        사람들은 이 문제가 단순 수학문제라서 레벨 1이라고 하는데
        나한텐 3 레벨 정도 되는듯.. ㅋㅋㅋㅋㅋㅋㅋㅋㅋ
    '''

    answer = []

    start = [startX, startY]

    for x, y in balls:

        if startX == x or startY == y:
            first_triangle_dist = 0
            second_triangle_dist = 0

            if startX == x:
                # 꼭지점의 좌표 구하기
                dot = abs(startY - y) / 2 + min(startY, y)
                # 거리 계산 
                # 꼭지점에 위치에 따른 거리 계산
                first_triangle_dist = (get_dist(start, [0, dot]) * 2) ** 2
                second_triangle_dist = (get_dist(start, [m, dot]) * 2) ** 2
            else:
                dot = abs(startX - x) / 2 + min(startX, x)
                first_triangle_dist = (get_dist(start, [dot, n]) * 2) ** 2
                second_triangle_dist = (get_dist(start, [dot, 0]) * 2) ** 2
            
            # 가까운 벽에 갔다가 오는 거리
            bounding_dist = 0
            if startX == x:
                if startY < y:
                    wall_dist = startY
                else:
                    wall_dist = n - startY
            else:
                if startX < x:
                    wall_dist = startX
                else:
                    wall_dist = m - startX
                
            dist = get_dist(start, [x, y])
            bounding_dist = (wall_dist * 2 + dist) ** 2

            print(first_triangle_dist, second_triangle_dist, bounding_dist)
            answer.append(round(min(first_triangle_dist, second_triangle_dist, bounding_dist)))

        else:
            # 이 외에는.....몰라 ㅋ
            answer.append(-1)

    return answer

print(solution(	10, 10, 3, 7, [[7, 7], [2, 7], [7, 3]]))



def solve(x, y, startX, startY, ballX, ballY):
    dists = []
    # 위쪽 벽
    # 단, x좌표가 같고 목표의 y가 더 크면 안된다.
    if not (ballX == startX and ballY > startY):
        d2 = (ballX - startX)**2 + (ballY - 2*y+startY)**2
        dists.append(d2)
    # 아래쪽 벽
    # 단, x좌표가 같고 목표의 y가 더 작으면 안된다.
    if not (ballX == startX and ballY < startY):
        d2 = (ballX - startX)**2 + (ballY + startY)**2
        dists.append(d2)
    # 왼쪽 벽에 맞는 경우
    # 단, y좌표가 같고 목표의 x가 더 작으면 안된다.
    if not (ballY == startY and ballX < startX):
        d2 = (ballX + startX)**2 + (ballY - startY)**2
        dists.append(d2)
    # 오른쪽 벽
    # 단, y좌표가 같고 목표의 x가 더 크면 안된다.
    if not (ballY == startY and ballX > startX):
        d2 = (ballX - 2*x+startX)**2 + (ballY - startY)**2
        dists.append(d2)
    
    return min(dists)
    
def firstSolu(m, n, startX, startY, balls):

    '''
        다른 사람 풀이
        https://www.ai-bio.info/programmers/169198

        친 공이 반사되는 벽을 기준으로 맞을 공의 위치를 대칭시켜서
        두 공의 직선 거리를 계산하면 친 공의 이동거리를 구할 수 있다고 함
        대신 위, 아래, 왼쪽, 오른쪽 벽으로 칠 수 있는지 확인을 해야한다고 함

        무슨 점대칭?? 선대칭?? 으로 했다는데.....
        난 모르겠다 진짜... ㅋㅋㅋ


    '''

    answer = []
    for ballX, ballY in balls:
        answer.append(solve(m, n, startX, startY, ballX, ballY))
    return answer