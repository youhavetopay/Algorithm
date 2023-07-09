from collections import deque

def solution(people, limit):

    '''
        나의 풀이
        사람의 몸무게와 보트의 제한 무게가 있을때
        최소로 필요한 보트의 개수를 구하는 문제

        나의 접근법
        문제 유형에 탐욕법이라고 되어 있어서
        탐욕 문제라는 것에 대한 힌트를 얻고 해서 그런지
        어렵지 않았음
        몸무게를 정렬한 후 deque에 담고
        몸무게가 높은 걸 우선으로 담고 
        남는 부분을 
        몸무게가 적은 걸 우선으로 담아서 하면 됨

        프로그래머스 2레벨 문제가 몇개 안남아서
        이거 먼저 다 풀자 ㅋㅋ
    '''

    answer = 0

    people.sort()
    queue = deque(people)

    while queue:

        now_weight = queue.pop()

        while queue and now_weight + queue[-1] <= limit:
            now_weight += queue.pop()
        
        while queue and now_weight + queue[0] <= limit:
            now_weight += queue.popleft()

        answer += 1
        print(queue, answer)

    return answer

print(solution([70, 50, 80, 50], 100))


def firstSolu(people, limit):

    '''
        다른 사람 풀이
        프로그래머스 다른 사람 풀이
        https://school.programmers.co.kr/learn/courses/30/lessons/42885/solution_groups?language=python3

        투포인터를 활용한 풀이

        나도 처음엔 투포인터로 해볼려다가 
        체크해야 할게 많은 것 같아서 deque로 했는데
        이렇게 깔끔하다니 ㅋㅋㅋ

        짝지은 횟수 만큼 전체 수에서 빼주면
        필요한 보트의 개수가 나옴 ㅋㅋㅋ
    '''

    answer = 0

    people.sort()

    a = 0
    b = len(people) - 1

    while a < b:
        if people[b] + people[a] < limit:
            a += 1
            answer += 1
        
        b -= 1
    
    return len(people) - answer