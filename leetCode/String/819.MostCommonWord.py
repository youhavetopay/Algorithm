# 819.Most Common Word
# 난이도 : ★☆
# 가장 흔한 단어

# 금지된 단러를 제외한 가장 흔하게 등장하는 단어를 출력하라.
# 대소문자 구분을 하지않으며, 구두점(마침표, 쉼표등) 또한 무시한다.
# 반환할 단어는 소문자로 반환하기


from typing import List

def mostCommonWord(paragraph: str, banned: List[str]) -> str:  # 나의 풀이

    word_dict = {}
    main_word = ''

    for word in paragraph:
        if word.isalpha(): # 특수문자와 문자를 구별하기 위해 문자를 따로 담음
            main_word += word
        
        else: # 특수문자가 아닐 때
            if main_word != '':  
                if main_word.lower() not in banned: # 금지문자가 아닐때 카운트
                    try:
                        word_dict[main_word.lower()] += 1
                    except KeyError:
                        word_dict[main_word.lower()] = 1
                main_word = ''

    if main_word != '': # 반복문이 끝났을 때 지금까지 담은 문자 카운트
        try:
            word_dict[main_word.lower()] += 1
        except KeyError:
            word_dict[main_word.lower()] = 1

    common_word = ''

    count = 0

    for key, value in word_dict.items(): # 가장 높은 카운트를 가지는 문자 찾기
        if count < value:
            common_word = key
            count = value

    return common_word

#print(mostCommonWord('Bob hit a ball, the hit BALL flew far after it was hit.', ["hit"]))

#print(mostCommonWord("Bob. hIt, baLl", ["bob", "hit"]))

#print(mostCommonWord("a, a, a, a, b,b,b,c, c", ["a"]))

print(mostCommonWord("Bob",[]))

import collections
import re
def mostCommonWord(paragraph: str, banned: List[str]) -> str:  # 첫번째 풀이

    # 정규표현식을 통해 문자(\w) 가 아닌 단어는 공백으로 변경 후 소문자로 치환하고 리스트로 변경한다.
    words = [word for word in re.sub(r'[^\w', ' ', paragraph)
        .lower().split() 
        if word not in banned]

    # collections 의 Counter를 통해 갯수 카운트
    counts = collections.Counter(words)
    return counts.most_common(1)[0][0] # 가장 흔하게 등장하는 단어 값을 반환
    # [('ball', 2) ...] 대충 이런식으로 저장되어 있음 

    counts = collections.defaultdict(int) # 딕셔너리 생성 초기값이 int인 형식으로
    for word in words: # 카운트
        counts[word] += 1
    return max(counts, key=counts.get) # 가장 value 가 큰 key를 가져옴