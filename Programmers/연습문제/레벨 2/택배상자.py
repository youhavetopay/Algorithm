def solution(order):

    '''
        나의 풀이
        스택형 대기열이 있을 때
        택배 순서를 주어진 순서에 맞게 몇개까지 
        보낼 수 있는지 계산하는 문제
        
        나의 접근법
        이거 그냥 문제 잘 읽어보면
        대놓고 스택이라고 되어 있어서
        사실상 그냥 문제의 요구사항대로 구현만 하면 됨

        막 엄청?? 어렵진 않았음
        스택을 알면 쉽게 풀 수 있는 문제인듯??
    '''

    now_order = 0
    stack = []

    box_idx = 1
    while box_idx < len(order) + 1:
                
        if box_idx == order[now_order]:
            now_order += 1
            box_idx += 1
        else:
            if stack and stack[-1] == order[now_order]:
                now_order += 1
                stack.pop()
            else:
                stack.append(box_idx)
                box_idx += 1
        

    while stack:
        if stack[-1] != order[now_order]:
            return now_order
        
        stack.pop()
        now_order += 1

    return len(order)


print(solution([1,2,3,4]))


def firstSolu(order):

    '''
        다른 사람 풀이
        프로그래머스 다른 사람 풀이
        https://school.programmers.co.kr/learn/courses/30/lessons/131704/solution_groups?language=python3

        같은 스택을 사용했다는 것에
        나랑 비슷하지만 이게 코드가 훨씬 간단해서
        더 좋은 풀이 인 듯??
    '''

    answer = 0
    stacks = []
    N = len(order)
    i = 1
    idx = 0
    while i < N + 1:
        stacks.append(i)
        while stacks[-1] == order[idx]:
            idx += 1
            stacks.pop()
            if len(stacks) == 0:
                break
        i += 1

    return idx