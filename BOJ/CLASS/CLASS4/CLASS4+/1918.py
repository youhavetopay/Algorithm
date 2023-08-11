
'''
    백준 1918. 후위 표기식
    중위 표기식으로 되어 있는 수식을 
    후위 표기식으로 바꾸는 문제
'''

import sys
input = sys.stdin.readline

def solution():

    '''
        나의 풀이

        나의 접근법
        와... 많이 어려웠음.. ㅋㅋㅋㅋ
        옛~~~~~~~날에 학교 알고리즘 시간에 전위, 중위, 후위 표기식에 대해 배운 것 같은데
        그때 스택을 사용했던 것 같았음.. ㅋㅋ
        그래서 대충 생각해보니까 스택으로 하면 될 것 같아서 해봤는데 너무 어려웠음 ㅋㅋ

        처음엔 스택 2개를 사용해서 피연산자, 연산자를 구분해서 스택에 담았는데
        피연산자 순서를 지정하는게 너~~~~~~~무 어려웠음
        먼저 나온 순서대로 해야하는데 스택에 담아버려서 피연산자의 원래 인덱스도 고려해야하나?? 
        아님 deque 를 사용해서 고려해야 하나?? 이런식으로 고민은 엄청 했었음...


        그렇게 코드를 몇번 갈아 엎고 하루 지나서 다시 보는데
        생각해보니 피연산자는 스택에 담을 필요가 없고 피연산자 순서는 중위나 후위나 순서는 똑같았음 ㅋㅋㅋㅋ

        그래서 피연산자는 계속 정답 문자열에 넣고
        연산자만 스택에 담아서 스택의 top 보다 우선순위가 높으면 담고
        아니면 높거나 같을때 까지 스택에서 pop 해주면서 정답 문자열에 담아주는 방식으로 함

        괄호가 있는 경우는 재귀로 해당 괄호가 끝날때까지 동일한 로직을 반복해주고
        끝나면 괄호가 끝난 다음부터 다시 순회하는 방식으로 풀었음.. ㅋㅋㅋㅋ

        스택을 활용하는 구현문제인데
        역시 골드 2 답다 ㅋㅋㅋㅋㅋ
    '''

    # 연산자 우선순위
    ordering = { '+':0, '-':0, '*' : 1, '/' : 1}

    in_fix = input().rstrip()

    # 시작 인덱스, 현재 후위표기식 문자열
    def make_post_fix(start_i, now_post_fix):

        i = start_i

        stack = []
        while i < len(in_fix):
            
            word = in_fix[i]

            # 괄호가 있으면 재귀
            if word == '(':
                post_fix, next_i = make_post_fix(i+1, '')
                now_post_fix += post_fix
                i = next_i
                continue

            # 괄호가 끝나면 반복문 나가기
            if word == ')':
                break
            
            # 연산자 인 경우
            if word in ordering:

                # 스택의 top 이랑 비교해서 담거나 빼주기
                if stack:
                    if ordering[stack[-1]] < ordering[word]:
                        stack.append(word)
                    else:
                        while stack and ordering[stack[-1]] >= ordering[word]:
                            now_post_fix += stack.pop()
                        stack.append(word)
                else:
                    stack.append(word)
            
            # 피연산자 인 경우 바로 정답 문자열에 담아주기
            elif word.isalpha():
                now_post_fix += word


            i += 1

        # 반복문이 끝나면 남아 있는 스택에 있는 연산자들 넣어주기
        while stack:
            now_post_fix += stack.pop()
        return now_post_fix, i+1
    
    post_fix, _ = make_post_fix(0, '')
    print(post_fix)
    return

# solution()




def firstSolu(sdaw):
    
    '''
        다른 사람 풀이
        https://pannchat.tistory.com/entry/%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EB%B0%B1%EC%A4%80-%ED%9B%84%EC%9C%84%ED%91%9C%EA%B8%B0%EC%8B%9D-python

        나랑 똑같이 스택으로 하심

        나랑 다른 점은
        괄호를 처리하는 방법이 조금 다름
        괄호도 스택 안에 넣어서 닫는 괄호가 나오면 열린 괄호가 나올때까지 계속 pop 해주는 방식?

        나머지는 곱셈과 나누기는 같은 우선순위를 가진 연산자가 있으면 계속 빼주고
        더하기랑 빼기는 괄호가 있거나 다 빼주는 방식으로 하심

        푸는 방식은 나랑 얼추 비슷한거 같은데
        웰케 간단하게 한거 같지?? ㅋㅋㅋㅋ

        내가 너무 이상하게 한듯/? ㅋㅋㅋ
    '''

    strn = list(sdaw)
    stack = []
    res = ''

    for s in strn:

        if s.isalpha():
            res += s
        else:
            if s == '(':
                stack.append(s)

            elif s == '*' or s == '/':
                while stack and (stack[-1] == '*' or stack[-1] == '/'):
                    res += stack.pop()
                stack.append(s)
            
            elif s == '+' or s == '-':
                while stack and stack[-1] != '(':
                    res += stack.pop()
                stack.append(s)
            
            elif s == ')':
                while stack and stack[-1] != '(':
                    res += stack.pop()
                stack.pop()
    
    while stack:
        res += stack.pop()
    

    return res

t = [
    ['A*(B+C)', 'ABC+*'],
    ['A+B', 'AB+'],
    ['A+B*C', 'ABC*+'],

    ['A+B*C-D/E', 'ABC*+DE/-'],
    ['A*(B+C)/D', 'ABC+*D/'],
    ['A+(B-C)/D', 'ABC-D/+'],

    ['A+B*C+D', 'ABC*+D+'],
    ['A+B*C', 'ABC*+'],
    ['A+B+C+D', 'AB+C+D+'],

    ['A+B*C+D*E+G', 'ABC*+DE*+G+'],
    ['A*B+C+D+E*F*G+E', 'AB*C+D+EF*G*+E+'],
    ['((A+B)*C)/D', 'AB+C*D/']

]

for i, tc in enumerate(t):
    result = firstSolu(tc[0])
    if result != tc[1]:
        print(result, tc[1], 'tc', i+1)
        print()