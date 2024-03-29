def solution(w,h):

    '''
        나의 풀이
        사각형을 대각선으로 나눴을 때
        넓이가 1인 정사각형이 몇개 나오는지 -> 잘린 부분은 빼고
        계산하는 문제

        나의 접근법
        일단 하나하나 체크해봤는데
        높이가 1이거나 너비가 1이면 하나도 없고
        만약 정사각형이라면 전체 사각형 개수에서 한 변의 길이만큼 빼주면 됨

        그리고 나머지에서는 예전에 풀었던 정수 좌표평면 개수 세는 걸 활용함
        대각선을 직선의 방정식이라고 생각하고 기울기와 y절편을 구함 
        그리고 x를 대입해보면서 정수의 좌표를 계산하고 더해주는 방식으로 품

        이거 좀 많이 어려웠음
        솔직히 수학관련해서는 너무 힘든듯
        하다보니까 결국 또 무식하게 전부 계산했긴 했는데
        고민한거에 비해 코드는 별게 없어서 좀 그럼 ㅋㅋ
    '''

    answer = 0

    # 너비나 높이가 1이면 올바른 정사각형 하나도 없음
    if w == 1 or h == 1:
        return 0
    
    # 정사각형 인 경우
    if w == h:
        return (w * h) - w
    
    # 기울기와 절편 구하기
    a, b = get_a_b(w ,h)
    
    # 1부터 x절편까지 구하기
    x = 1
    while x < w:
        
        # 만족하는 정수값이 해당 라인의 정사각형의 개수
        max_y = a * x + b
        answer += int(max_y)
        x += 1

    # 한쪽만 구했고 대칭이니까 곱하기 2
    return answer * 2

def get_a_b(w, h):
    b = h

    a = -b / w

    return a, b

print(solution(5, 5))


def gcd(a,b):
    return b if (a == 0) else gcd(b%a, a)

def firstSolu(w, h):

    '''
        다른 사람 풀이
        프로그래머스 다른 사람 풀이
        https://school.programmers.co.kr/learn/courses/30/lessons/62048/solution_groups?language=python3

        교점 수=반복되는 횟수=(최대공약수)/ 교점이 없을 때 대각선이 뚫는 사각형 개수=(가로'+세로'-1)/ (가로'+세로'-1)*(최대공약수)=(가로+세로-최대공약수)/ 답: 전체사각형 개수-(가로+세로-최대공약수)

        예를 들어, w = 8, h = 12 라고 해봅시다. 
        이 때, g = gcd(w, h) = 4, w' = w/g = 2, h' = h/g = 3 라고 해봅시다. 
        w'xh' (= 2x3) 종이에서 지워지는 블록의 개수를 계산하고 g(=4)를 다시 곱해주면 wxh(= 8x12) 종이에서 지워지는 블록의 개수를 얻을 수 있습니다. 
        
        이제 w'xh'인 종이에서 지워지는 블록의 개수를 생각해봅시다. 

        잘 생각해보면 i열에서 지워지는 블록들과 (i+1)열에서 지워지는 블록들은 오로지 한 행만 공유한다는 사실을 알 수 있습니다. 
        따라서 w' x h' 종이에서 지워지는 블록의 개수는 w'+h'-1 이 됩니다. 
        결국 전체 종이에서 지워지는 블록의 개수는 g*(w'+h'-1) = g*(w/g + h/g - 1) = w + h -g 가 됩니다.
        

        그렇다고 함..
    '''

    return w*h - w - h + gcd(w, h)