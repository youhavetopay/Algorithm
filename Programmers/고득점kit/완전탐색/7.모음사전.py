def solution(word):

    '''
        나의 풀이
        중복 조합?? 순열?? 을 구해서 순서를 찾는 문제

        그냥 단어 처음부터 끝까지 전부 만들어서
        정렬하면 사전순으로 정렬이 됨
        그 후 해당 단어의 index를 찾아서 반환하는 방식으로 품 ㅋㅋ

        처음에 단어 순서가 이해가 안되서 
        좀 이해하는데 좀 걸렸음 ㅋㅋㅋㅋㅋㅋㅋ

        대충 5중첩 for 문 인데
        단어 수가 많지 않아서 대충 5^5 정도??
        그냥 풀리는듯..
    '''
    # 단어들을 구성하는 알파벳들
    words = ['A', 'E', 'I', 'O', 'U']

    # 모든 단어들
    total_words = set()

    def makeWord(now_word, max_length):

        # 목표 길이에 단어가 완성되면 넣어주기
        if len(now_word) == max_length:
            total_words.add(now_word)
            return 
        
        # 모든 단어 구하기
        for w in words:
            makeWord(now_word + w, max_length)
    
    # 길이는 1 ~ 5 까지
    for i in range(1, 6):
        makeWord('', i)

    # 사전순으로 정렬
    sorted_words = sorted(list(total_words))

    # index + 1 해주기
    return sorted_words.index(word) + 1

print(solution('AAAE'))


import itertools

def firstSoul(word):

    '''
        다른 사람 풀이
        https://alreadyusedadress.tistory.com/297

        파이썬에 itertools.product 라는 기능을 사용해서
        모든 중복 순열을 구하고
        나머지는 나랑 똑같음

        나도 풀면서 파이썬에서 왠지 이런걸 구해주는 기능이 있을 것 같았는데
        몰라서 그냥 직접 구현함 ㅋㅋㅋ
    '''

    words = []

    for i in range(1, 6):
        for c in itertools.product(['A', 'E', 'I', 'O', 'U'], repeat=i):
            words.append(''.join(list(c)))

    words.sort()

    return words.index(word) + 1


def secondSoul(word):

    '''
        두번째 다른 사람 풀이
        프로그래머스 다른 사람 풀이
        https://school.programmers.co.kr/learn/courses/30/lessons/84512/solution_groups?language=python3

        등비수열의 합을 이용한 풀이라고 함 ㅋㅋㅋㅋ
    '''

    answer = 0

    for i, n in enumerate(word):
        answer += (5 ** (5 - i) - 1) / (5 - 1) * 'AEIOU'.index(n) + 1

    return answer