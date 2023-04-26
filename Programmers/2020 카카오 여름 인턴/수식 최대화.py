import itertools

def calculator(operator, a, b):
    if operator == '+':
        return a + b
    elif operator == '-':
        return a - b
    elif operator == '*':
        return a * b

def getExpressionResult(order, expression):

    for operator in order:

        while operator in expression:
            idx = expression.index(operator)
            result = calculator(expression[idx], expression[idx-1], expression[idx+1])
            expression[idx+1] = result
            expression.pop(idx-1)
            expression.pop(idx-1)

    return abs(sum(expression))

def solution(expression):

    '''
        나의 풀이
        연산자의 우선순위를 바꾸면서 수식의 절대값의 최대값을 계산하는 문제

        나의 접근법
        연산자와 피연산자를 구분하고
        연산자들을 중복 없이 순열로 구함 -> 우선순위
        그 후 우선순위에 따라 수식을 계산하는 방식으로 품

        연산자가 +, -, * 이렇게 밖에 없고
        예외처리 할 필요 없고
        수식 전체의 길이가 100 이하라서
        구현만 할줄 알면 쉽게 풀듯 함
    '''

    answer = 0

    operators = set()

    split_expression = []

    word = ''
    for w in expression:
        if w.isnumeric():
            word += w
        else:
            operators.add(w)
            split_expression.append(int(word))
            split_expression.append(w)
            word = ''

    if word:
        split_expression.append(int(word))

    operators_order = set(itertools.permutations(operators, len(operators)))


    for order in operators_order:
        answer = max(answer, getExpressionResult(order, split_expression[:]))

    return answer

print(solution("100-200*300-500+20"))


def firstSolu(expression):

    '''
        다른 사람 풀이
        프로그래머스 다른 사람 풀이

        eval이라는 것을 사용해서 엄청 깔끔하게 풀어냄 ㄷㄷ
        디게 깔끔하게 푸신듯?? ㅋㅋㅋ
    '''

    # 연산자의 우선순위를 미리 구해둠 ㅋㅋ
    operations = [('+', '-', '*'),('+', '*', '-'),('-', '+', '*'),('-', '*', '+'),('*', '+', '-'),('*', '-', '+')]
    answer = []

    for op in operations:
        # 첫번째 연산자
        a = op[0]
        # 두번째 연산자
        b = op[1]
        temp_list = []

        # 첫번째 연산자를 기준으로 분리
        for e in expression.split(a):

            # 두번째 연산자를 기준으로 분리
            temp = [f"({i})" for i in e.split(b)]
            # 두번째 연산자를 사이에 괄호를 넣어줌
            temp_list.append(f'({b.join(temp)})')
        
        # 첫번째 연산자를 사이에 괄호를 넣어주고 문자열로된 수식??을 계산
        answer.append(abs(eval(a.join(temp_list))))
    
    return max(answer)