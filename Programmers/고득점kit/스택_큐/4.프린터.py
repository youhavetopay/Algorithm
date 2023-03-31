import collections

def solution(priorities, location):

    '''
        나의 풀이
        우선순위 큐를 구현하는 문제

        deque를 사용해서 품
        데이터 크기가 100까지라서 문제에서 구현하라는데로 구현해도
        무리없이 통과함

        처음엔 단순한 우선순위큐를 구현하면 되는 줄 알아서 
        heap을 사용했지만 우선순위가 높지 않은 작업의 경우 빼서 뒤로 다시 넣어야 하는데
        그렇게 되면 우선순위가 같을 때는 heap으로 안되서 
        그냥 deque로 깡 구현함 ㅋㅋ
    '''


    answer = 0
    queue = collections.deque([idx, priority] for idx, priority in enumerate(priorities))

    while queue:

        idx, priority = queue[0]

        if max([pri for _, pri in queue]) != priority:
            queue.append([idx, priority])

        else:
            answer += 1
            if idx == location:
                break
        
        queue.popleft()
        

    return answer

print(solution([2, 1, 3, 2], 2))


def firstSoul(priorities, location):

    '''
        다른 사람 풀이
        https://eda-ai-lab.tistory.com/461

        나랑 똑같이 deque를 사용한 풀이
        근데 우선순위 값을 앞으로 해서 queue에 넣어두니
        max를 할때 그냥 queue를 넣어도 되서 코드가 훨씬 깔끔해진듯??

        굳이 넣는 순서가 중요하진 않으니까 나중에 보기 좋은대로 하는게
        좋을 듯 함
    '''

    answer = 0

    d = collections.deque([v, i] for i, v in enumerate(priorities))

    while len(d):
        item = d.popleft()

        if d and max(d)[0] > item[0]:
            d.append(item)
        else:
            answer += 1
            if item[1] == location:
                break

    return answer