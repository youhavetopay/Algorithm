def solution(brown, yellow):

    '''
        나의 풀이
        색깔별 타일 개수가 주어지면 사각형의 너비와 높이를 구하는 문제
        단 노란색 타일은 겉에 있을 수 없고 무조건 갈색 타일이 둘러 쌓여있어야 함

        정수의 너비와 높이를 가지는 사각형이라서
        곱해서 총 넓이가 되는 수를 찾으면 됨        
        
        처음에 또 문제를 제대로 안읽어서
        만들 수 있는 사각형이 여러개 나와서 이게 뭐야..?? 라고 생각했었음 ㅋㅋㅋㅋㅋㅋ
        타일의 색깔별 개수가 주어지면 무조건 하나만 나오게 됨 ㅋㅋ

        예전에 풀었던 문제인데
        예전에는 갈색의 개수를 맞추는 방식으로 품 ㅋㅋㅋ

    '''

    answer = []

    # 총 넓이
    total_area = brown + yellow

    # 최소 높이 -> 갈색이 둘러 쌓고 있어야 해서
    height = 3
    width = total_area // height
    
    print(width, height)

    # 너비랑 같거나 높을 때까지
    while width >= height:

        # 너비와 높이가 정수 일때
        if total_area % height == 0:

            # 노란색 타일 개수 구하기
            # 맨 윗줄,  맨 아랫줄 제거 
            # 맨 왼쪽 줄, 맨 오른쪽 줄 제거
            # 갈색으로 둘러쌓여있기 때문에
            yellow_count = (width - 2) * (height - 2)

            if yellow_count == yellow:
                return [width, height]
        
        # 높이를 1 올리기
        height += 1
        width = total_area // height

        print(width, height)

    return answer

print(solution(10,2))


def firstSoul(brown, yellow):
    
    '''
        다른 사람 풀이
        https://iambeginnerdeveloper.tistory.com/123

        노란색 타일이 직사각형이여야 한다는 걸 초점으로 품
        
        노란색 타일 가로 * 2 + 노란색 타일 세로 * 2 + 4 = 갈색 타일 개수
        라는 식을 사용해서 품 ㄷㄷ

        노란색 타일을 기준으로 갈색 타일의 수를 찾는건 
        좀 떠올리기 힘든 풀이법인듯...
    '''

    answer = []

    yellow_x = 0
    yellow_y = 0

    for i in range(1, yellow + 1):
        if yellow % i == 0:
            yellow_x = int(yellow / i)
            yellow_y = i

            if yellow_x * 2 + yellow_y * 2 + 4 == brown:
                answer.append(yellow_x + 2)
                answer.append(yellow_y + 2)

                return sorted(answer, reverse=True)
            
    return answer


import math
def secondSoul(brown, yellow):

    '''
        다른 사람 풀이
        https://school.programmers.co.kr/learn/courses/30/lessons/42842/solution_groups?language=python3
        프로그래머스 다른 사람 풀이

        길이, 넓이 공식 각각으로 식 두개를 만들고
        변수 두개 존재하니까 이차방정식으로 근의 공식 사용한 풀이.............

        대충 근의 공식 사용한 풀이법??

        풀이 신기해서 가져와봄
    '''

    w = ((brown + 4) / 2 + math.sqrt(((brown+4) / 2) ** 2 - 4 * (brown + yellow))) / 2
    h = ((brown + 4) / 2 - math.sqrt(((brown + 4) / 2) ** 2 - 4 * (brown + yellow))) / 2

    return [w, h]