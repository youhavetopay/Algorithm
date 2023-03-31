def solution(s):

    '''
        나의 풀이
        올바른 괄호인지 체크하는 문제

        너무 많이 풀어서 
        이제는 너무 쉬움
        그래도 스택의 기본중 기본 문제이니
        잘 익혀두자 ㅎㅎ
    '''

    stack = []

    for word in s:

        if word == '(':
            stack.append(word)
        elif not stack:
            return False
        elif stack[-1] == '(':
            stack.pop()
        else:
            return False

    return len(stack) == 0

def firstSoul(s):

    '''
        다른 사람 풀이
        https://a-littlecoding.tistory.com/122

        스택 대신 숫자로 괄호를 체크함
        괄호의 종류가 하나일 때는 괜찮을듯???
    '''

    answer = 0

    for c in s:
        if c == '(':
            answer += 1
        else:
            if answer > 0:
                answer -= 1
            else:
                return False
    if answer > 0:
        return False
    
    return True