# # 937. Reorder Log Files
# 난이도 : ★
# 로그파일 재정렬

# 로그를 재정렬하라. 기준은 다음과 같다
# 1. 로그의 가장 앞 부분은 식별자이다.
# 2. 문자로 구성된 로그가 숫자 로그보다 앞에 온다.
# 3. 식별자는 순서에 영향을 끼치지 않지만 문자가 동일할 경우 식별자 순으로 한다.
# 4. 숫자 로그는 입력 순서대로 한다.


from typing import List

def reorderLogFiles(logs: List[str]) -> List[str]:  # 나의 풀이

    digit_list = []  # 숫자 로그를 담을 리스트
    answer = [] # 정답
    word_dict = {} 

    for idx, word in enumerate(logs):
        
        title = ''
        startIdx = 0
        for i, w in enumerate(word):  # 로그의 식별자와 로그값을 분리
            if w == ' ':
                startIdx = i
                break
            title += w

        log_msg = word[startIdx+1:]

        if log_msg[0].isdigit(): # 로그값이 숫자라면 입력 순서대로 따로 저장하기
            digit_list.append(word)
        else:
            try:
                word_dict[log_msg].append([title, idx]) # 로그값을 바탕으로 식별자와 idx를 저장
            except KeyError:
                word_dict[log_msg] = [[title[0], idx]]

    sorted_dict_keys = sorted(list(word_dict.keys())) # 로그값을 기준으로 정렬

    

    for key in sorted_dict_keys: 
        if len(word_dict[key]) > 1: #로그값이 같을 경우 식별자를 기준으로 다시 정렬
            word_dict[key] = sorted(word_dict[key])

        for values in word_dict[key]: # 문자 로그 먼저 정답에 추가
            answer.append(logs[values[1]])
    
    answer += digit_list # 따로 저장해둔 숫자로그 뒤에 추가

    return answer


print(reorderLogFiles(["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]))


print(reorderLogFiles(["j mo", "5 m w", "g 07", "o 2 0", "t q h"]))


def reorderLogFiles(logs: List[str]) -> List[str]:  # 첫번째 풀이 람다를 통한 정렬 우선순위를 적용

    digits = [] 
    letters = []

    for log in logs:
        if log.split()[1].isdigit(): # split을 통해 로그값이 문자인지 숫자인지 판별
            digits.append(log)
        else:
            letters.append(log)

    letters.sort(key=lambda x:(x.split()[1:], x.split()[0])) # 람다식을 통해 로그값 첫번째, 식별자를 두번째로 해서 정렬 ㄷㄷ

    return letters + digits