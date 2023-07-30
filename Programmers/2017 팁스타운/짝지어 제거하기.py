
'''
    프로그래머스 짝지어 제거하기
    짝수로 붙어있는 문자열을 제거할 수 있을때
    모든 문자열을 제거할 수 있는지 확인하는 문제
'''


def solution(s):

    '''
        나의 풀이

        나의 접근법
        스택을 사용해서 이전문자열이랑 같으면 빼주면서 
        반복하였음

        스택에 담고 다음번에는 해당 스택을 다시 새로운 스택을 사용해서
        이전과 같은 로직을 하고

        스택이 모두 비워졌다면 모든 문자를 제거한 것
        만약 이전 스택이랑 현재 스택이랑 길이가 같다면 -> 붙어있는 같은 문자가 없음
        문자를 제거할 수 없는 상태로 했음

        이러니까 풀림 ㅋㅋㅋ

        솔직히 시간복잡도에서 걸릴 줄 알았는데 
        생각보다 쉽게 통과해서 의야 했음

        보니까 이전에 풀어둔 것도 있는데 확인해 봐야겠다 ㅋㅋㅋ
    '''

    last_stack = s

    while True:
        stack = []

        for word in last_stack:
            if stack and stack[-1] == word:
                stack.pop()
            else:
                stack.append(word)
        
        if stack == []:
            return 1
        
        if len(last_stack) == len(stack):
            return 0
        
        last_stack = stack


def firstSolu(s):

    '''
        다른 사람 풀이
        프로그래머스 다른 사람 풀이
        https://school.programmers.co.kr/learn/courses/30/lessons/12973/solution_groups?language=python3

        아 ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ
        굳이 while 문으로 반복하지 않아도
        어차피 스택에 남아있으므로 한번만 순회하면 됨 ㅋㅋㅋㅋㅋㅋㅋㅋㅋ
    '''
    
    temp = ["",s[0]]

    for i in s[1:]:
        if temp[-1]!=i:
            temp.append(i)
        else:
            temp.pop()

    return 1 if len(temp)==1 else 0



def lastSolu(s):

    '''
        예전에 내가 풀던 풀이?? ㅋㅋㅋㅋ

        스택을 사용을 했는데
        같은 문자 제거하는걸 이상하게 함 ㅋㅋㅋ
        스택에 담겨있던 마지막 문자로만 같은 문자를 체크해서
        틀린듯? ㅋㅋㅋ
    '''

    answer = 1

    stack = []

    for word in s:
        
        if len(stack) > 1:
            if stack[-1] != word:
                count = 1
                last_word = stack.pop()
                while len(stack) >= 1 and last_word == stack[-1]:
                    stack.pop()
                    count += 1
                
                if count == 1:
                    stack.append(last_word)
        
        stack.append(word)

    
    last_word = stack.pop()
    count = 1
    while len(stack) >= 1 and last_word == stack[-1]:
        stack.pop()
        count += 1
    
    if count == 1:
        stack.append(last_word)
    
    if len(stack):
        answer = 0


    return answer