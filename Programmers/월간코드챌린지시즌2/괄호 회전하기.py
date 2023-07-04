from collections import deque

def solution(s):

    '''
        나의 풀이
        괄호 문자열이 주어지면
        왼쪽으로 1칸씩 회전시키면서 괄호가 올바른지 체크하는 문제

        나의 접근법
        deque랑 stack 잘 활용하면 쉽게 풀 수 있음

        괄호체크가 stack 기본 문제라서 어렵지 않았음
        그래서 그런지 맞춰도 1점밖에 안줌 ㅋㅋ
    '''

    answer = 0

    i = 0
    queue = deque(list(s))
    
    while i < len(s):
        if check(queue):
            answer +=1
        
        queue.append(queue.popleft())
        i += 1

    return answer

def check(queue):

    stack = []

    for w in queue:
        if not stack and w in [')', '}', ']']:
            return False
        
        if w in ('(', '{', '['):
            stack.append(w)
        else:

            if stack[-1] == '(' and w == ')':
                stack.pop()
            elif stack[-1] == '{' and w == '}':
                stack.pop()
            elif stack[-1] == '[' and w == ']':
                stack.pop()
            
            else:
                return False
    
    if stack:
        return False
    return True


print(solution("[](){}"))



def firstSolu(s):

    '''
        다른 사람 풀이
        프로그래머스 다른 사람 풀이
        https://school.programmers.co.kr/learn/courses/30/lessons/76502/solution_groups?language=python3

        ㅋㅋㅋㅋ
        replace로 정말 신기하게 했음 ㅋㅋㅋ
        저렇게 많이 한 이유는 아마도 s의 길이가 최대 1000 이라서 그런듯 ㅋㅋㅋㅋㅋ
        대박 ㅋㅋ
        아 그리고 이 코드에서 좋은 부분은 
        문자열의 길이가 홀수일때는 전부 다 틀린 괄호이기 때문에
        저렇게 처리해준 부분이 보기 좋았음
        나도 다음엔 저렇게 해야지 ㅋㅋ
    '''

    tmp_s = s
    answer = 0

    if len(s) % 2 == 1: return answer

    for i in range(len(s)):
        t = tmp_s.replace("()", "").replace("{}", "").replace("[]", "")

        t = t.replace("{}", "").replace("[]", "").replace("()", "")
        t = t.replace("[]", "").replace("()", "").replace("{}", "")
        t = t.replace("()", "").replace("{}", "").replace("[]", "")
        t = t.replace("{}", "").replace("[]", "").replace("()", "")
        t = t.replace("[]", "").replace("()", "").replace("{}", "")
        t = t.replace("()", "").replace("{}", "").replace("[]", "")
        t = t.replace("{}", "").replace("[]", "").replace("()", "")
        t = t.replace("[]", "").replace("()", "").replace("{}", "")
        t = t.replace("()", "").replace("{}", "").replace("[]", "")
        t = t.replace("{}", "").replace("[]", "").replace("()", "")
        t = t.replace("[]", "").replace("()", "").replace("{}", "")
        t = t.replace("()", "").replace("{}", "").replace("[]", "")
        t = t.replace("{}", "").replace("[]", "").replace("()", "")
        t = t.replace("[]", "").replace("()", "").replace("{}", "")
        t = t.replace("()", "").replace("{}", "").replace("[]", "")
        t = t.replace("{}", "").replace("[]", "").replace("()", "")
        t = t.replace("[]", "").replace("()", "").replace("{}", "")
        t = t.replace("()", "").replace("{}", "").replace("[]", "")
        t = t.replace("{}", "").replace("[]", "").replace("()", "")
        t = t.replace("[]", "").replace("()", "").replace("{}", "")
        t = t.replace("()", "").replace("{}", "").replace("[]", "")
        t = t.replace("{}", "").replace("[]", "").replace("()", "")
        t = t.replace("[]", "").replace("()", "").replace("{}", "")
        t = t.replace("{}", "").replace("[]", "").replace("()", "")
        t = t.replace("[]", "").replace("()", "").replace("{}", "")
        t = t.replace("()", "").replace("{}", "").replace("[]", "")
        t = t.replace("{}", "").replace("[]", "").replace("()", "")
        t = t.replace("[]", "").replace("()", "").replace("{}", "")
        t = t.replace("()", "").replace("{}", "").replace("[]", "")
        t = t.replace("{}", "").replace("[]", "").replace("()", "")
        t = t.replace("[]", "").replace("()", "").replace("{}", "")
        t = t.replace("()", "").replace("{}", "").replace("[]", "")
        t = t.replace("{}", "").replace("[]", "").replace("()", "")
        t = t.replace("[]", "").replace("()", "").replace("{}", "")
        t = t.replace("()", "").replace("{}", "").replace("[]", "")
        t = t.replace("{}", "").replace("[]", "").replace("()", "")
        t = t.replace("[]", "").replace("()", "").replace("{}", "")
        t = t.replace("()", "").replace("{}", "").replace("[]", "")
        t = t.replace("{}", "").replace("[]", "").replace("()", "")
        t = t.replace("[]", "").replace("()", "").replace("{}", "")
        t = t.replace("()", "").replace("{}", "").replace("[]", "")
        t = t.replace("{}", "").replace("[]", "").replace("()", "")
        t = t.replace("[]", "").replace("()", "").replace("{}", "")
        t = t.replace("()", "").replace("{}", "").replace("[]", "")
        t = t.replace("{}", "").replace("[]", "").replace("()", "")
        t = t.replace("[]", "").replace("()", "").replace("{}", "")
        t = t.replace("()", "").replace("{}", "").replace("[]", "")
        t = t.replace("{}", "").replace("[]", "").replace("()", "")
        t = t.replace("[]", "").replace("()", "").replace("{}", "")
        t = t.replace("()", "").replace("{}", "").replace("[]", "")
        t = t.replace("{}", "").replace("[]", "").replace("()", "")
        t = t.replace("[]", "").replace("()", "").replace("{}", "")
        t = t.replace("()", "").replace("{}", "").replace("[]", "")
        t = t.replace("{}", "").replace("[]", "").replace("()", "")
        t = t.replace("[]", "").replace("()", "").replace("{}", "")
        t = t.replace("()", "").replace("{}", "").replace("[]", "")
        t = t.replace("{}", "").replace("[]", "").replace("()", "")
        t = t.replace("[]", "").replace("()", "").replace("{}", "")
        t = t.replace("()", "").replace("{}", "").replace("[]", "")
        t = t.replace("{}", "").replace("[]", "").replace("()", "")
        t = t.replace("[]", "").replace("()", "").replace("{}", "")
        t = t.replace("()", "").replace("{}", "").replace("[]", "")
        t = t.replace("{}", "").replace("[]", "").replace("()", "")
        t = t.replace("[]", "").replace("()", "").replace("{}", "")
        t = t.replace("()", "").replace("{}", "").replace("[]", "")
        t = t.replace("{}", "").replace("[]", "").replace("()", "")
        t = t.replace("[]", "").replace("()", "").replace("{}", "")
        t = t.replace("()", "").replace("{}", "").replace("[]", "")
        t = t.replace("{}", "").replace("[]", "").replace("()", "")
        t = t.replace("[]", "").replace("()", "").replace("{}", "")
        t = t.replace("()", "").replace("{}", "").replace("[]", "")
        t = t.replace("{}", "").replace("[]", "").replace("()", "")
        t = t.replace("[]", "").replace("()", "").replace("{}", "")
        t = t.replace("()", "").replace("{}", "").replace("[]", "")
        t = t.replace("{}", "").replace("[]", "").replace("()", "")
        t = t.replace("[]", "").replace("()", "").replace("{}", "")
        t = t.replace("()", "").replace("{}", "").replace("[]", "")
        t = t.replace("{}", "").replace("[]", "").replace("()", "")
        t = t.replace("[]", "").replace("()", "").replace("{}", "")
        t = t.replace("()", "").replace("{}", "").replace("[]", "")
        t = t.replace("{}", "").replace("[]", "").replace("()", "")
        t = t.replace("[]", "").replace("()", "").replace("{}", "")
        t = t.replace("()", "").replace("{}", "").replace("[]", "")

        if t == "":
            answer += 1

        tmp_s = tmp_s[1:] + tmp_s[0]

    return answer