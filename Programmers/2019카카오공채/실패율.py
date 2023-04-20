import collections

def solution(N, stages):

    '''
        나의 풀이
        스테이지 도달 정보에 따른 해당 스테이지 실패율을 계산해서
        실패율이 높은 순으로 정렬하는 문제

        나의 접근법
        Counter 기능을 통해 각각의 스테이지의 도달 정보를 기록하고
        1번 스테이지 부터 N번째 스테이지까지 실패율을 계산하는 방법으로 품

        레벨 1 문제임에도 불구하고 오래걸림...
        처음엔 해당 스테이지를 통과한사람, 통과 못한 사람을 전부 기록해서 하니
        시간초과 겁나뜨고 틀린 답이 나온게 많아서 전부 갈아엎고 다시 풀기를 시작함 ㅋㅋ
        생각해보니 통과한 사람을 다 기록할 필요는 없기 때문에 Counter로 쉽게 풀 수 있었음

        예전에도 푼적이 있는데 이때는 Counter를 몰라서
        1 ~ N 까지 계속 count(n) 으로 했었음 ㅋㅋㅋ
        그래서 시간복잡도도 1000ms까지 나온듯 ㅋㅋㅋ

    '''
    
    answer = []

    stages_counter = collections.Counter(stages)

    print(stages_counter)
    now_player_count = len(stages)
    fail_scores = []

    for stage in range(1, N+1):

        if stage not in stages_counter:
            fail_scores.append([stage, 0])
        else:

            if now_player_count > 0:
                fail_scores.append([stage, stages_counter[stage] / now_player_count])
                now_player_count -= stages_counter[stage]
            else:
                fail_scores.append([stage, 0])

    fail_scores.sort(key=lambda x:(-x[1], x[0]))
    answer = [i for i, value in fail_scores]

    return answer

print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]	))


def firstSolu(N, stages):

    '''
        다른 사람 풀이
        프로그래머스 다른 사람 풀이
        https://school.programmers.co.kr/learn/courses/30/lessons/42889/solution_groups?language=python3

        나의 풀이랑 약간 비슷한데
        count를 계속 하는 부분이 차이점이 있음
        시간복잡도는 높은 대신에 코드 자체는 훨씬 깔끔한듯? ㅋㅋㅋ
    '''

    result = {}
    denominator = len(stages)

    for stage in range(1, N+1):
        if denominator != 0:
            count = stages.count(stages)
            result[stage] = count / denominator
            denominator -= count
        else:
            result[stage] = 0
    
    return sorted(result, key=lambda x: result[x], reverse=True)