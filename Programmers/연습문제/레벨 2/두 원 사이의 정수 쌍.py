def get_dist_origin(x, y):

    return ((x ** 2) + (y ** 2)) ** (1/2)

def get_circle_dot_count(r):

    count = 0
    circle_on = 0

    x, y = r, 0

    while y <= r:

        while get_dist_origin(x, y) > r:
            x -= 1
        count += x + 1
            
        if get_dist_origin(x, y) == r:
            circle_on += 1

        y += 1
 
    total = (count * 2 - 1) + ((count - (r * 2) - 1) * 2)
    circle__on_total = circle_on * 2 + ((circle_on - 2) * 2)
    
    
    return [total, circle__on_total]


def solution(r1, r2):

    '''
        나의 풀이
        반지름 두개가 주어지면 큰 원과 작은 원 사이의 
        정수의 위치값을 가지는 좌표의 개수를 카운팅 하는 문제
        (원 위에 있는 좌표도 포함)

        나의 접근법
        처음엔 반지름당 가지는 좌표의 개수를 구해서
        해볼려고 했으나 점화식?? 을 모르겠어서 포기..

        그 후엔 0,0 ~ r,r 까지 전부 탐색하고 해보려고 했으나
        시간초과가 떴었음

        그래서 생각한 방법이
        y값을 0 ~ r까지 1씩 증가 시키면서
        x값은 r ~ 0 까지 탐색 
        만약 (x, y) 가 만족하면 (x-1, y), (x-2, y), ... (0, y) 는 전부 만족하는 좌표 이므로
        해당 개수를 더해주고
        탐색하면서 원 위에 있는 좌표는 따로 개수를 카운팅해줌

        그 후 큰원의 좌표개수와 작은 원의 자표개수를 빼주고 작은 원에 원 위에 있는 좌표값을
        더해주면 정답이 나옴

        진짜 또 거의 3시간 가까이 품....
        진짜 심각하다.. ㅠㅠ 수학 부분은 너~~~~~~무 부족한듯..
        이번껀 문제가 문제가 아니라 내가 너무 문제인듯 ㅋㅋㅋㅋㅋ
    '''

    answer = 0

    r1_dot = get_circle_dot_count(r1)
    r2_dot = get_circle_dot_count(r2)

    print(r1_dot, r2_dot)

    answer = r2_dot[0] - r1_dot[0] + r1_dot[1]

    return answer


print(solution(999999, 1000000))

from math import sqrt

def firstSolu(r1, r2):

    '''
        다른 사람 풀이
        https://velog.io/@error_io/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EB%91%90-%EC%9B%90-%EC%82%AC%EC%9D%B4-%EC%A0%95%EC%88%98%EC%9D%98-%EC%8C%8D-Lv.2-Python

        풀이 엄청 간단할 것 같더라...ㅋ
        근데 이해 1도 안감... 뭐지.. ㅋㅋㅋㅋㅋㅋ
        한쪽만 구해서 * 4해주는 것 까진 이해 했는데
        자세히는 모르겠ㅇㅁ...
    '''

    quar = 0
    for i in range(0, r2):
        quar += int(sqrt(r2**2 - i**2)) - int(sqrt(max(0, r1**2 - i**2 - 1)))
    return quar * 4