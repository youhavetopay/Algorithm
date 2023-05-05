# 신규아이디 추천
import re

def solution(new_id):
    answer = ''

    # 1단계
    answer = new_id.lower() # 소문자로 대문자는 upper
    
    #2단계
    answer = re.sub(r"[^a-zA-Z0-9._-]","", answer)  # 정규표현식 
    

    #3단계
    while '...' in answer or '..' in answer:
        if '...' in answer:
            dot3 = answer.index('...')
            answer = answer[0:dot3] + '.' + answer[dot3+3:]
            
        if '..' in answer:
            dot2 = answer.index('..')
            answer = answer[0:dot2]+'.'+answer[dot2:]
    

    #4단계
    if answer[0] == '.':
        answer = answer[1:]
    

    #5단계
    if answer == '':
        answer = answer + 'a'
    


    #6단계
    if len(answer) >= 16:
        answer = answer[:15]
    
    if answer[-1] == '.':
        answer = answer[:-1]
    

    #7단계
    if len(answer) <= 2:
        while len(answer) < 3:
            answer = answer + answer[-1]
    

    return answer


name = "z-+.^."
print(solution(name))