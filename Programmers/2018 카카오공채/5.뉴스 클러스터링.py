import collections
import re


def getWords(string):

    words = collections.defaultdict(int)
    for i in range(len(string)+1):

        check_word = string[i-2: i]

        if check_word.isalpha():
            words[check_word.lower()] += 1

    return words


def solution(str1, str2):
    
    '''
        나의 풀이
        문자열의 자카드 계수를 계산하는 문제

        파이썬의 dict자료형을 사용하니 그래도??
        쉽게 풀렸음 ㅋㅋㅋ
    '''

    answer = 0

    # 문자열을 2개로 끊어서 
    # dict자료형을 만듬(문자 key, 개수 value)
    str1_words = getWords(str1)
    str2_words = getWords(str2)

    # 둘다 문자가 없다면 끝내기
    if len(str1_words.keys()) == 0 and len(str2_words.keys()) == 0:
        return 65536

    print(str1_words)
    print(str2_words)


    inter_count = 0
    union_count = 0

    # 교집합의 개수 찾기
    for key in list(str1_words.keys()):

        if key in str2_words:
            if str1_words[key] < str2_words[key]:
                inter_count += str1_words[key]
                str2_words[key] -= str1_words[key]
                del str1_words[key]

            elif str1_words[key] > str2_words[key]:
                inter_count += str2_words[key]
                str1_words[key] -= str2_words[key]
                del str2_words[key]
            else:
                inter_count += str1_words[key]
                del str1_words[key]
                del str2_words[key]

    # 남아있는 값들의 합과 교집합의 합이 합집합의 개수
    union_count = sum(str1_words.values()) + sum(str2_words.values()) + inter_count

    print(str1_words)
    print(str2_words)

    print(inter_count, union_count)

    answer = int((inter_count / union_count) * 65536)
    
    return answer

str1 = 'FRANCE'
str2 = '123'

print(solution(str1, str2))



def solution(str1: str, str2: str) -> str:

    '''
        책 풀이
        와우 ㅋㅋㅋ 역시 코드 깔끔함 ㅋㅋㅋ
        Counter를 통해 계산함
    '''

    # 정규표현식으로 알파벳만 골라서 넣어줌
    str1s = [
        str1[i:i+2].lower()
        for i in range(len(str1) - 1)
        if re.findall('[a-z]{2}', str1[i:i+2].lower())
    ]

    str2s = [
        str2[i:i+2].lower()
        for i in range(len(str2) - 1)
        if re.findall('[a-z]{2}', str2[i:i+2].lower())
    ]

    # Counter 객체끼리 교집합 구하기
    intersection = sum(
        (
            collections.Counter(str1s) & collections.Counter(str2s)
        ).values()
    )

    # Counter 객체끼리 합집합 구하기
    union = sum(
        (
            collections.Counter(str1s) | collections.Counter(str2s)
        ).values()
    )
    
    # 자카드 계수 구하기
    jaccard_sim = 1 if union == 0 else intersection / union
    return int(jaccard_sim * 65536)