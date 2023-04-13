import collections

def solution(begin, target, words):

    '''
        나의 풀이
        주어진 단어가 목표 단어로 변할 때 규칙에 따라 몇번 변해야 하는지
        계산하는 문제

        나의 접근 법
        단어를 정점으로 하고 해당 단어에서 변경될 수 있는 단어들을 이어줌 -> 그래프
        중복된 단어는 없다고 했으니 그래프로 만들 수 있음
        그래프를 만들고 나서 그냥 BFS로 최단거리 계산해주면 끝
        
        테스트케이스에 의하면 단어가 없을 때만 단어를 못만들고
        단어끼리는 무조건 만들 수 있게 된듯?? -> 그래프가 무조건 하나만 나오는듯 함

        그래프를 만드는 과정을 떠올리기 힘들었음 ㅋㅋ
        그 외에는 BFS라서 쉬웠지만
        단어끼리 변경될 수 있는 걸 그래프로 구현하는게 어려웠음
        아마 문제 유형이 없었다면 풀기 힘들었을 듯...

    '''

    # 못 만드는 단어 일 때
    if target not in words:
        return 0
    
    # 그래프 생성
    # 단어 목록에 시작 단어 넣어주기
    graph = collections.defaultdict(list)
    words.append(begin)

    # 그래프 만들어주기
    for idx, word in enumerate(words):

        for i in range(idx+1, len(words)):
            count = 0

            # 이거 문제 있음 ㅋㅋㅋ
            # 테스트케이스 상으론 단어의 길이가 모두 같은 경우만 있는것 같은데
            # 만약 다르면 indexErorr 뜸 ㅋㅋㅋ
            # max_length = max(len(word), len(words[i])) 

            # for j in range(max_length):
            #     if word[j] != words[i][j]:
            #         count += 1
            
            for a, b in zip(word, words[i]):
                if a != b:
                    count += 1

            # 단어 일치도가 한 개 이하일 때만 넣어줌
            # -> 해당 단어로 변경될 수 있을 때
            if count < 2:
                graph[word].append(words[i])
                graph[words[i]].append(word)

    # 거리 dict 초기화
    keyword_dist = {}
    for word in words:
        if word == begin:
            keyword_dist[word] = 0
        else:
            keyword_dist[word] = float('inf')

    queue = collections.deque()
    now_dist = 0
    queue.append([begin])

    # BFS 시작
    while queue:

        now_words = queue.popleft()
        next_words = []
        for word in now_words:
            for keyword in graph[word]:
                if keyword_dist[keyword] == float('inf'):
                    next_words.append(keyword)
                    keyword_dist[keyword] = min(now_dist + 1, keyword_dist[keyword])
        
        if next_words:
            queue.append(next_words)
        
        now_dist += 1

    print(keyword_dist)


    return keyword_dist[target]

print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))


def get_adjacent(current, words):
    for word in words:

        # 단어 길이 다를땐 패스
        if len(current) != len(word):
            continue

        count = 0
        for c, w in zip(current, words):
            if c != w:
                count += 1
        
        if count == 1:
            yield word



def firstSoul(begin, target, words):

    '''
        다른 사람 풀이
        프로그래머스 다른 사람 풀이
        https://school.programmers.co.kr/learn/courses/30/lessons/43163/solution_groups?language=python3

        나랑 비슷한데 yield 이라는 것을 사용해서
        해당 단어에서 변경될 수 있는 단어들을 찾는 과정을 따로 함수로 만들었음
        훨씬 보기 깔끔한듯??
    '''

    dist = {begin: 0}
    queue = collections.deque([begin])

    while queue:

        current = queue.popleft()

        for next_word in get_adjacent(current, words):
            if next_word not in dist:
                dist[next_word] = dist[current] + 1
                queue.append(next_word)

    # 해당 key가 없을 때 0으로 가져오기
    return dist.get(target, 0)