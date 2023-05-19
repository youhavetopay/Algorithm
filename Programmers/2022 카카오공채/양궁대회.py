def solution(n, info):

    '''
        나의 풀이
        어피치가 쏜 양궁 결과가 주어지면
        라이언이 점수차를 가장 크게 이기는 
        양궁 결과를 반환하는 문제

        나의 접근법
        라이언이 점수를 얻을 수 있는 모든?? 경우의 수를 구하고
        비교하는 방식으로 품

        생각보다 어려웠음 ㅋㅋ
        단순히 최대 점수차를 구하라고 하면
        이것보단 좀 더 간단했을듯?ㅋㅋㅋ

    '''

    # 어피치 보다 최소 차이로 이길 수 있는 
    # 각 점수별 필요 화살 갯수 구하기
    min_win_count = []

    for i in range(len(info)):
        min_win_count.append(info[i]+1)

    combinations = []

    # DFS로 조합 구하기
    def dfs(now, left_arrow, last_idx):
        
        # 모든 화살을 사용했다면 조합에 넣어주기
        if left_arrow == 0:
            combinations.append(now)
            return
        
        for i in range(last_idx + 1, len(min_win_count)):
            # 해당 점수를 이길 수 있다면 넣어주기
            if left_arrow - min_win_count[i] >= 0:
                dfs(now + [i], left_arrow - min_win_count[i], i)
            else:
                # 못 이기면 여기까지 한거 넣어주기
                dfs(now, 0, i)


    dfs([], n, -1)

    max_score = 0
    answer = [-1]

    # 경우 별 점수 계산하기
    for combi in combinations:

        # 라이언의 양궁 결과 계산하기
        rion_score_board = [0] * 11
        left_arrow = n
        for score in combi:
            left_arrow -= min_win_count[score]
            rion_score_board[score] = min_win_count[score]

        # 화살이 남았다면 0점에 화살 전부 넣어주기
        # 점수차이가 같은게 여러개면 낮은 점수를 많이 맞춘게 정답이기 때문
        if left_arrow > 0:
            rion_score_board[-1] = left_arrow

        # 라이언이랑 어피치 점수 계산하기
        apich_score = 0
        rion_score = 0
        for i in range(len(info)-1):
            if info[i] >= rion_score_board[i] and info[i] != 0:
                apich_score += 10 - i
            
            if rion_score_board[i] > info[i]:
                rion_score += 10 - i

        # 라이언이 이길때만 계산
        if rion_score > apich_score:
            # 현재 점수 차이가 더 클때
            if max_score < rion_score - apich_score:
                answer = rion_score_board
                max_score = rion_score - apich_score

            # 점수 차이가 같다면 가장 낮은 점수를 더 많이 맞친게 정답
            elif max_score == rion_score - apich_score:
                for i in range(len(info)-1, -1, -1):
                    if answer[i] < rion_score_board[i]:
                        answer = rion_score_board
                        break
                    elif answer[i] > rion_score_board[i]:
                        break

    return answer

print(solution(10, [0, 0, 0, 0, 0, 0, 0, 0, 3, 4, 3]))

def firstSolu(n, info):

    '''
        다른 사람 풀이
        프로그래머스 다른 사람 풀이
        https://school.programmers.co.kr/learn/courses/30/lessons/92342/solution_groups?language=python3

        나랑 비슷한 접근법으로 푸심
        대신 훨씬 깔끔하게 푸신듯 함
        dfs로 라이언이 쏠수 있는 경우의 수를 계산함
        대신 0점 부터 채워 넣는 방식으로
        그 후 어피치와의 점수차이를 계산하는 방식으로 품


        라이언 이름이... 저거였네 ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ
        어피치도......ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ
    '''

    global answer, result

    # 점수 차이 계산하기
    def score(ryan):
        s = 0
        for i in range(11):
            if ryan[i] == info[i] == 0:
                continue
            # 라이언 획득
            if ryan[i] > info[i]:
                s += 10 - i
            # 어피치 획득 -> 라이언 점수에서 빼주기
            else:
                s -= 10 - i
        
        return s
    
    def dfs(idx, left, ryan):
        global answer, result

        if idx == -1 and left:
            return
        
        # 화살을 모두 사용한 경우
        if left == 0:
            s = score(ryan)
            if result < s:
                answer = ryan[:]
                result = s
            return
        
        # 사용할 수 있는 화살을 하나씩 빼면서 체크
        for i in range(left, -1, -1):
            ryan[idx] = i
            dfs(idx - 1, left - i, ryan)
            ryan[idx] = 0

    answer = [0 for _ in range(11)]
    result = 0
    dfs(10, n, [0 for _ in range(11)])

    return answer if result != 0 else [-1]
