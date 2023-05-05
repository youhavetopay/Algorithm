import sys
from collections import defaultdict

sys.setrecursionlimit(20_000)

def getTrie(words):

    trie = {}

    for word in words:

        pointer = trie
        for i, w in enumerate(word):
            if w not in pointer:
                pointer[w] = {}
            
            pointer = pointer[w]
            if i == len(word)-1:
                pointer['end'] = True

    return trie


def solution(words, queries):

    '''
        나의 풀이
        쿼리가 매칭되는 words의 개수를 계산하는 문제

        나의 접근법
        Trie 사용해서 품
        단순히 트라이만 해서는 효율성에서 통과를 못해서 약간의 최적화를 해줌


        Trie 개념이 좀 어려운 개념인가??
        레벨 4 치곤 엄청 빨리 품
        최근에 푼 레벨 3 문제 보다 훨씬 빨리 푼듯..
    '''

    # 정답 리스트 초기화
    answer = [0] * len(queries)

    # querie가 중복될 수 있다고 해서
    # 한번 계산하면 다시 안하도록 dict에다 저장
    word_counter = {}

    # ?으로만 이루어진 querie도 있기 때문에 
    # word의 길이별로 카운팅 해줌
    word_length_counter = defaultdict(int)
    
    # 트라이 만들기
    trie = getTrie(words)

    reversed_words = []
    for word in words:
        word_length_counter[len(word)] += 1
        reversed_words.append(list(reversed(list(word))))

    # ?은 접두어 혹은 접미어로 있기 때문에
    # 접두어로 있는 경우 ? 으로 탐색하면 너무 많기 때문에
    # 문자를 뒤집어서 트라이로 만들고 queire도 뒤집어서 검색하면 훨씬 빠름
    reversed_word_trie = getTrie(reversed_words)

    # DFS로 탐색
    def dfs(now_pointer, querie, querie_idx, word_idx):

        # querie의 끝까지 탐색을 했을 경우
        # 끝내기
        if word_idx == len(querie):
            if 'end' in now_pointer:
                answer[querie_idx] += 1
            return
        
        # 현재 문자가 ? 인 경우 해당 레벨에서 모든 단어로 검색을 해야함
        if querie[word_idx] == '?':
            
            for word in now_pointer.keys():
                if word == 'end':
                    continue
                next_pointer = now_pointer[word]
                dfs(next_pointer, querie, querie_idx, word_idx + 1)

        else:
            if querie[word_idx] in now_pointer:
                next_pointer = now_pointer[querie[word_idx]]
                dfs(next_pointer, querie, querie_idx, word_idx + 1)

        return
    
    # querie 별로 검색 시작
    for querie_idx, querie in enumerate(queries):

        querie_length = len(querie)

        # ? 으로만 이루어진 querie라면 길이가 같은 word를 넣어줌
        if querie == '?' * querie_length:
            if querie_length in word_length_counter:
                answer[querie_idx] = word_length_counter[querie_length]

            continue

        # 이미 계산한 querie인지 체크
        if querie not in word_counter:

            # ? 이 접두어로 있으면 뒤집어서 검색하기
            if querie[0] == '?':
                dfs(reversed_word_trie, list(reversed(list(querie))), querie_idx, 0)
            else:
                dfs(trie, querie, querie_idx, 0)

            word_counter[querie] = answer[querie_idx]
        else:
            answer[querie_idx] = word_counter[querie]
        

    return answer

print(solution(["frodo", "front", "frost", "frozen", "frame", "kakao"], ["fro??", "????o", "fr???", "fro???", "pro?"]))


def firstSolu(words, queries):

    '''
        다른 사람 풀이
        https://velog.io/@hope1213/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EA%B0%80%EC%82%AC%EA%B2%80%EC%83%89-%ED%8C%8C%EC%9D%B4%EC%8D%AC

        나랑 비슷하게 트라이를 사용해서 품
        대신 트라이에 단어들의 길이를 넣어서
        ? 만나면 거기서 바로 끝내도록 해서 훨씬 빠를듯??

        근데 직접 돌려보니 큰 차이는 없는듯.. ㅋㅋ
        어쨋든 아이디어는 디게 좋은듯 함
        파이썬 dict에는 자료형 제한 없이 아무거나 들어갈 수 있다는게 가장 큰 포인트 인듯 함 ㅋㅋ
    '''

    head, head_rev = {}, {}
    wc = []

    def add(head, word):
        node = head
        for w in word:
            if w not in node:
                node[w] = {}
            
            node = node[w]
            if 'len' not in node:
                node['len'] = [len_word]
            else:
                # 단어들의 길이를 저장
                node['len'].append(len_word)
        
        node['end'] = True
    
    for word in words:
        len_word = len(word)
        add(head, word)
        add(head_rev, word[::-1])
        wc.append(len_word)
    
    def search(head, querie):
        count = 0
        node = head

        for q in querie:
            if q == '?':
                # querie에서 ? 만나면 그 뒤는 무조건 ? 만 나오니
                # 현재 위치에서 len의 count를 함 ㄷㄷ
                return node['len'].count(len_qu)
            elif q not in node:
                break

            node = node[q]
        
        return count
    
    li = []
    for querie in queries:
        len_qu = len(querie)
        if querie[0] == '?':
            if querie[-1] == '?':
                li.append(wc.count(len_qu))
            else:
                li.append(search(head_rev, querie[::-1]))
        else:
            li.append(search(head, querie))
    
    return li