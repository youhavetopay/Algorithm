def solution(n, l, r):


    '''
        나의 풀이(못품...ㅠㅠ)
        유사 칸토어 비트열?? 을 만드는데
        해당 n번째 칸토어 비트열에서 일정 구간에 1이 몇개 있는지 계산하는 문제

        나의 접근법
        만들어서 해볼려고 했으나.. 당연히 실패 ㅋㅋㅋ 최대 문장 길이가 5^20  ㅋㅋㅋㅋ
        문자가 (n-1 칸토어 * 2) + 0 * (5^(n-1)) + (n-1 칸토어 * 2) 요런식으로 반복되어서
        분할정복?? 으로 풀어보려고 했으나 시간 부족으로 포기...
        그리고 너무 어렵게 접근한듯...
        
        나름 반복되는 규칙은 빠르게 찾았지만
        이를 풀이까지 이어가는데는 실패함..ㅠㅠ
        이런 문제는 너무 어려운듯..
    '''

    answer = 0

    cantor = '1'
    idx = 0

    print(l // (5 ** (n-1)), l % (5 ** (n-1)), (5 ** (n-1)))
    print()
    print(r // (5 ** (n-1)), r % (5 ** (n-1)), (5 ** (n-1)))

    left_section = l // (5 ** (n-1))
    left_index = l % (5 ** (n-1))

    right_seciton = r // (5 ** (n-1))
    right_index = r % (5 ** (n-1))

    if left_index == 0 and right_index == (5 ** (n-1)):
        for i in range(left_section, right_seciton+1):
            if i == 2:
                continue
            
            answer += 4 ** n
        return answer

    # while idx < n:
    #     cantor = (cantor * 2) + ('0' * (5 ** (idx)) ) + (cantor * 2)
    #     idx += 1
    

    return answer

print(solution(2, 4, 17))


def firstSolu(n, l, r):

    '''
        다른 사람 풀이
        프로그래머스 질문하기 답
        https://school.programmers.co.kr/questions/49643

        아....
        내가 구한 공식처럼 
        0, 1, 2, 3, 4 이렇게 5개의 구역으로 나눠지는데
        무조건 2번 위치는 0임
        그래서 i % 5 == 2면 0이고
        다른 구간이라면 이전 칸토어로 이동해서 다시 반복해서 찾음
        그렇게 해서 i 가 5보다 작아질때까지 반복체크

        분할정복인듯????
    '''

    answer = 0

    # left 부터 right까지 검사
    for l in range(l-1, r):
        if check(l):
            answer += 1
    
    return answer

def check(i):

    # 중간 부분일때 -> 무조건 0
    if i % 5 == 2:
        return False
    
    # 더 이상 나눌 수 없을 때 -> 무조건 1
    if i < 5:
        return True
    
    # 이전 칸토어 문자에서 찾기
    return check(i // 5)