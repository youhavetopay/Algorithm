def get_dist(x, y):

    return ((x**2) + (y**2)) ** (1/2)

def solution(k, d):

    '''
        나의 풀이
        등차수열? ㅋㅋㅋ 으로 증가하는 좌표값이 있을 때
        원점으로 부터 d 거리 이하인 자연수로 이루어진 좌표의 개수를 구하는 문제

        나의 접근법
        예전에 두 원 사이의 정수 쌍 에서 하듯이 
        최대 X, 0 에서 부터 하나하나 다 탐색함 ㅋㅋㅋ
        
        솔직히 시간초과나 틀릴 줄 알았는데
        바로 통과해서 의야했음 ㅋㅋ
    '''

    answer = 0

    max_x = d

    # max_x 가 k의 배수될때까지 만들기
    while max_x % k != 0:
        max_x -= 1
    
    max_y = max_x

    now_x = max_x
    now_y = 0

    # 아래서부터 위로 탐색
    while now_y <= max_y:

        print(now_x, now_y)

        # 현재거리가 d보다 크면 x 를 빼주기
        while now_x > 0 and get_dist(now_x, now_y) > d:
            now_x -= k

        # x가 0 이면 (0, now_y) 밖에 없음
        if now_x == 0:
            answer += 1
        else:
            # (0, now_y), (k, now_y), (2k, now_y), .... 이렇게
            answer += (now_x // k) + 1
        
        # now_y 높이기
        now_y += k
        print(now_x, now_y, answer)
        print()

    return answer


print(solution(1, 5))


def fristSolu(k, d):

    '''
        다른 사람 풀이
        프로그래머스 다른 사람 풀이
        https://school.programmers.co.kr/learn/courses/30/lessons/140107/solution_groups?language=python3

        훨씬 간단함 ㅋㅋㅋ
        이래서 수학문제는 좀... ㅋㅋ

        1사분면에 사분원을 그린다고 생각하면 x^2 + y^2 = d^2 가 그려진다고 함 ㅋㅋ
        x = 0 부터 x += k를 하면서 y값을 구함
        y = 0 부터 y += k 하면서 sqrt(y) 와 같거나 작을때까지 count를 더한다고 함

        대충 원의 방정식 사용한거 같은데 정확히 뭔소리인지... ㅋㅋㅋㅋㅋ
    '''

    answer = 0
    for i in range(0, d+1, k):
        max_y = d*d - i*i
        answer += int(max_y ** 0.5)//k + 1
    return answer