def solution(words):

    '''
        나의 풀이
        문자열을 입력할때 중복되지 않는 접두어를 입력할때까지
        입력해야하는 문자의 개수를 계산하는 문제

        나의 접근법
        트라이 사용해서 품
        접두어 문제인걸 알고 트라이로 하니까 풀림...


        근데 솔직히 단어들의 길이 총합이 최대 100만이라길래
        시간초과 뜰 줄 알았음 ㅋㅋ
        근데 한번에 통과해서 좀 어이 없었음 ㅋㅋㅋ
    '''
    
    answer = 0

    trie = {}

    # 트라이 만들기
    for word in words:
        pointer = trie
        for w in word:
            if w not in pointer:
                pointer[w] = {}

            pointer = pointer[w]

            # 현재까지 누적된 접두어?? 기록하기
            if 'count' in pointer:
                pointer['count'] += 1
            else:
                pointer['count'] = 1
            
        print(trie)    
        
        
    print()
    for word in words:
        pointer = trie[word[0]]
        answer += 1
        for i in range(1, len(word)):
            print(word[i], pointer, pointer['count'])
            
            # 현재까지의 접두어로 만들 수 있는 문자가 하나일때 
            # 해당 단어 입력 끝내기
            if pointer['count'] == 1:
                break
            
            # 아니라면 더 깊게 들어가기
            pointer = pointer[word[i]]
            answer += 1


    return answer

print(solution(["go", "gone", "guild"]))





class Trie():
    def __init__(self) -> None:
        self.next = dict()
        self.value = 0


def firstSolu(words):

    '''
        다른 사람 풀이
        프로그래머스 다른 사람 풀이

        나랑 비슷하게 트라이를 사용해서 품
        대신 트라이를 클래스를 통해 좀 더 깔끔하게 정의한듯..
    '''

    answer = 0
    tree = Trie()

    for word in words:
        subtree = tree
        for idx, val in enumerate(word):
            subtree.value += 1
            if val not in subtree.next:
                subtree.next[val] = Trie()
            
            subtree = subtree.next[val]
            if idx == len(word) - 1:
                subtree.val += 1
    
    for word in words:
        subtree = tree
        counts = 0

        for idx, val in enumerate(word):
            if subtree.value == 1:
                answer += counts
                break
            
            elif idx == len(word) - 1:
                answer += counts + 1
                break

            else:
                subtree = subtree.next[val]
                counts += 1
    
    return answer


def secondSolu(words):

    '''
        다른 사람 풀이 2
        프로그래머스 다른 사람 풀이
        
        단어들을 사전순으로 정렬한 다음
        인접한 단어들을 비교하는 방식으로 품
    '''

    answer = 0
    words.sort()

    for idx, word in enumerate(words):
        res = 1
        if idx > 0:
            for i, char in enumerate(word):
                res = max(res, i + 1)
                if len(words[idx-1]) == i or words[idx-1][i] != char: break
        
        if idx + 1 < len(words):
            for i, char in enumerate(word):
                res = max(res, i + 1)
                if len(words[idx + 1]) == i or words[idx+1][i] != char: break
        
        answer += res

    return answer