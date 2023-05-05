OPEN = '('
CLOSE = ')'

def check(s):

    # 올바른 괄호 체크는
    # 스택으로 구현함

    stack = []
    for w in s:
        if w == OPEN:
            stack.append(w)
        else:

            if not stack or stack[-1] == CLOSE:
                return False
            else:
                stack.pop()

    return not stack

def reverseBracket(u):
    reversed_u = ''

    for w in u:
        if w == OPEN:
            reversed_u += CLOSE
        else:
            reversed_u += OPEN
    
    return reversed_u

def solution(p):

    '''
        나의 풀이
        짝이 맞는 괄호 문자열이 주어지면
        정해진 알고리즘에 따라 올바른 괄호로 변환하는 문제

        나의 접근법
        그냥 문제에서 구현하라는데로 구현함 ㅋㅋ

        엄청 명시적으로 알고리즘이 주어져서
        구현 문제이기 때문에 어렵지 않았음
    '''
    # 괄호 개수를 세는 counter
    counter = {OPEN:0, CLOSE:0}

    u = ''
    for i, w in enumerate(p):
        counter[w] += 1
        u += w

        # 괄호의 개수가 같다면
        if counter[OPEN] == counter[CLOSE]:
            
            # 문자열을 u, v로 나누기

            # v는 재귀 하기
            v = solution(p[i+1:])

            # u가 올바른 괄호 문자라면 u + v 해서 끝내기
            if check(u):
                return u + v
            else:
                # 아니라면 정해진 규칙에 따라 더해서 끝내기
                u = reverseBracket(u[1:-1])
                return OPEN + v + CLOSE + u
            
    # p가 빈 문자열일 때
    return ''

print(solution("(()())()"))


def firstSolu(p):

    '''
        다른 사람 풀이
        프로그래머스 다른 사람 풀이

        구현 문제라서 나랑 비슷한 풀이임
        근데.........
        너무 라인을 줄여서 읽기가 힘듬 ㅋㅋㅋㅋㅋ
        참 파이써닉 한데... ㅋㅋㅋ
    '''

    if p == '' : return p

    r = True
    c = 0

    for i in range(len(p)):

        # +1 -1을 하면서 괄호의 개수를 카운팅 함
        if p[i] == '(': c -= 1
        else: c += 1

        if c > 0: r = False

        if c == 0:
            if r:
                return p[:i+1]+firstSolu(p[i+1:])
            else:
                return '(' + firstSolu(p[i+1:]) + ')' + ''.join(list(map(lambda x: '(' if x == '(' else ')', p[1:i])))