def solution(files):
    
    '''
        나의 풀이
        파일 명을 분리해서 정렬하는 문제

        나의 접근법??
        그냥 문제대로 구현함... ㅋㅋ
        파일 이름을 head, number, tail 로 분리해서
        리스트에 index와 함께 담아줌
        그리고 head, number, index 순으로 정렬하는 방식으로 품
        
        문제 자체는 어렵지 않았는데
        문제를 제대로 읽질 않아서 생각보다 오래걸림 ㅋㅋ

        그리고 head를 추출하는 과정에서 실수가 있어서
        제대로 못풀고 있었는데 결국 질문하기에서 힌트를 얻어서 고침...
        다음 부터는 시간이 걸리더라도 혼자서 좀 해결해보도록 하자..!!
    '''

    answer = []

    file_info = []

    for i, file in enumerate(files):

        head = ''
        number = ''
        tail = ''

        for w in file:
            # number가 비어있고 숫자가 아닐때 head에 넣어주기
            if not w.isdigit() and number == '':
                head += w.lower()

            # 숫자이고 head는 있고 tail은 비었을 때 넣어주기
            elif w.isdigit() and head and tail == '':
                number += w
            # head와 number가 존재할 때 는 다 tail에다 넣어주기
            elif head and number:
                tail += w.lower()
        
                        
        file_info.append([i, head, int(number), tail])
        
    # 해당 순으로 정렬
    file_info.sort(key=lambda x:(x[1], x[2], x[0]))
    for i, head, number, tail in file_info:
        answer.append(files[i])

    return answer

# print(solution(  ["img10.zip", "img10.png", "img2.png", "img1.png"]))


import re

def firstSoul(files):

    '''
        다른 사람 풀이
        프로그래머스 다른 사람 풀이
        https://school.programmers.co.kr/learn/courses/30/lessons/17686/solution_groups?language=python3

        와우.. 정규표현식을 통해 디게 깔끔하게 품 ㄷㄷ
        참 파이써닉 하게 푸신듯 ㅋㅋㅋ
    '''    

    # 연결된 숫자들을 모두 찾고 첫번째 숫자(=number)를 기준으로 정렬
    a = sorted(files, key=lambda file: int(re.findall('\d+', file)[0]))
    print(a)
    # 숫자를 기준으로 나눠서 맨 앞에(=head) 문자를 기준으로 정렬.. ㅋㅋㅋ
    b = sorted(a, key=lambda file : re.split('\d+', file.lower())[0])

    return b

print(firstSoul(["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]))