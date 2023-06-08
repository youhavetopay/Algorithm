from collections import deque

def solution(x, y, n):

    '''
        나의 풀이
        숫자를 목표 숫자로 만드는데 필요한 최소 연산의 횟수를 구하는 문제

        나의 접근법
        처음에 그냥 DFS로 전부 했는데
        재귀 깊이 때문에 런타임에러 떠서 이건 아니다 라고 생각해서
        반대로 접근함 
        x -> y로 만드는게 아니라 y -> x로 만들어서 해봄 
        => y -> x로 하면 정수가 아닌건 후보에서 제외되기 떄문에 조금 더 효율적

        그렇게 하니까 조금 나아지긴 했는데 그래도 여전히 뜨길래
        일단 BFS로 바꿔서 시간초과가 뜨는게 보고 싶어서
        이때 y -> x로 계속하는게 아니라 다시 x -> y 로 해버려서 고민하게 됨
        그러다가 결국 힌트 봤는데 역시나 y -> x로 하는게 맞았고
        힌트보니까 중복된 숫자는 다시 큐에 안넣을려고 set으로 중복검사를 함
        그렇게 하니 통과....

        아 억울함... 한 5분만 더 생각해볼껄....
        좀만 더 고민했었으면 힌트 안보고 풀 수 있었는디....ㅠㅠㅠㅠ
    '''

    if x == y:
        return 0

    queue = deque()
    queue.append([y - n, 1])
    queue.append([y / 2, 1])
    queue.append([y / 3, 1])

    visited = set()

    while queue:

        now, count = queue.popleft()

        if now == x:
            return count
        
        nexts = [now - n, now / 2, now / 3]
        for next in nexts:
            if next >= x and next == int(next) and int(next) not in visited:
                queue.append([int(next), count + 1])
                visited.add(int(next))
    
    return -1


print(solution(2, 5, 4))


def firstSolu(x, y, n):

    '''
        다른 사람 풀이
        프로그래머스 다른 사람 풀이

        역시나... set으로 중복을 제거하는게 핵심이였음.. ㅠㅍㅍ
    '''

    answer = 0
    s = set()
    s.add(x)

    while s:
        if y in s:
            return answer
        
        nxt = set()
        for i in s:
            if i + n <= y:
                nxt.add(i+n)
            if i * 2 <= y:
                nxt.add(i * 2)
            if i * 3 <= y:
                nxt.add(i * 3)

        s = nxt
        answer += 1

    return -1