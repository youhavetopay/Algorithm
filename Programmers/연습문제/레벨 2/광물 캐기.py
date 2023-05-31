# def calc_total_fatigue(picks, minerals, max_get_mine):

#     now_fatigue = 0
#     minerals_idx = 0
#     picks_idx = 0
#     while picks_idx < len(picks) and minerals_idx < len(minerals):

#         now_durability = 5
#         while now_durability > 0 and picks_idx < len(picks) and minerals_idx < len(minerals):

#             now_fatigue += calc_fatigue(picks[picks_idx], minerals[minerals_idx])
#             now_durability -= 1
#             minerals_idx += 1
        
#         picks_idx += 1

#     if minerals_idx < len(minerals) and minerals_idx + 1 < max_get_mine:
#         return float('inf')
    
#     return now_fatigue


# def get_min_fatigue(total_picks, minerals):

#     fatigue = [float('inf')]

#     max_get_mine = len(total_picks) * 5

#     def dfs(select_idxs, selected_picks):

#         now_fatigue = calc_total_fatigue(selected_picks, minerals, max_get_mine)
        
#         if now_fatigue != float('inf') or len(selected_picks) == len(total_picks):
#             fatigue[0] = min(fatigue[0], now_fatigue)
#             return
        
#         for i in range(len(total_picks)):
#             if i not in select_idxs:
#                 select_idxs.add(i)
#                 dfs(select_idxs, selected_picks + [total_picks[i]])
#                 select_idxs.remove(i)
                
    
#     dfs(set(), [])

#     return fatigue[0]


def solution(picks, minerals):

    '''
        나의 풀이(진짜 완~~~~~~전 뻘짓함 ㅋㅋㅋㅋ)
        순서대로 광물을 캘때 곡갱이에 따른 피로도를 계산해서
        곡갱이를 모두 사용하거나 모든 광물을 캤을때
        가장 낮은 피로도를 구하는 문제

        나의 접근법
        처음엔 곡갱이 선택 순서를 순열로 모두 체크했는데 
        -> ex) 1, 2, 3 이라면 (0, 1, 1, 2, 2, 2), (1, 0, 1, 2, 2, 2) .... 이렇게
        5, 5, 5 이렇게 입력이 들어오니까 순열의 개수가 너~~~~~~무 많아져서 (15! 정도?)
        또한 피로도를 계산하는 것도 너무 비효율적인 것 같아서

        다른 방법을 생각해봄

        일단 무조건 곡갱이를 한번 선택하면 5개는 캐야해서 
        광물들을 5개 단위로 나눔
        그 후 dfs로 찾는 방법을 사용했는데
        바보같이 dfs 함수 안에서 광물을 for문으로 돌려서 시간초과가 계속 떠서
        계속 삽질하다가 겨우 풀게 됨 ㅜㅜ

        진짜 레벨 2인데 왤케 어렵게 푸는지....ㅠㅠ

    '''

    # total_picks = []

    # kind = 0
    # for pick in picks:
    #     i = 0
    #     while i < pick:
    #         total_picks.append(kind)
    #         i += 1
    #     kind += 1


    # return get_min_fatigue(total_picks, minerals)


    # 광물들을 5개 단위로 나누기
    split_minerals = []
    i = 0
    while i < len(minerals):

        temp = []
        while len(temp) < 5 and i < len(minerals):
            temp.append(minerals[i])
            i += 1
        split_minerals.append(temp)

    # 최소 피로도
    answer = [float('inf')]


    def dfs(now_picks, now_minerals_idx, now_fatigue):
        
        # 곡갱이를 모두 사용했거나 모든 광물을 캤을 때
        if now_picks == [0, 0, 0] or now_minerals_idx == len(split_minerals):
            print(now_picks, now_minerals_idx, now_fatigue)
            # 최소 값 갱신
            answer[0] = min(answer[0], now_fatigue)
            return
        
        # 곡갱이 선택
        for pick_kind, pick in enumerate(now_picks):
            if pick > 0:
                next_pick = now_picks[:]
                next_pick[pick_kind] -= 1

                dfs(next_pick, now_minerals_idx+1, now_fatigue + calc_total_fatigue(pick_kind, split_minerals[now_minerals_idx]))

    print(split_minerals)
    dfs(picks[:], 0, 0)

    return answer[0]

def calc_total_fatigue(pick, minerals):

    total_fatigue = 0
    for mine in minerals:
        total_fatigue += calc_fatigue(pick, mine)
    
    return total_fatigue

def calc_fatigue(pick, mine):

    if pick == 0:
        return 1
    elif pick == 1:
        if mine == 'diamond':
            return 5
        
        return 1
    else:
        if mine == 'diamond':
            return 25
        elif mine == 'iron':
            return 5
        
        return 1

print(solution(	[1, 3, 2], ["diamond", "diamond", "diamond", "iron", "iron", "diamond", "iron", "stone"]))


def firstSolu(picks, minerals):

    '''
        다른 사람 풀이
        프로그래머스 다른 사람 풀이
        https://school.programmers.co.kr/learn/courses/30/lessons/172927/solution_groups?language=python3

        나랑 거의 똑같이 품
        차이점이라면 나 처럼 광물을 따로 나누는게 아니라
        앞에 5개 부분만 보고 다음 걸로 넘어간다는 차이점?
        그리고 피로도 계산을 아주 깔끔하게 하심

    '''

    def solve(picks, minerals, fatigue):
        if sum(picks) == 0 or len(minerals) == 0:
            return fatigue
        
        result = [float('inf')]

        for i, fatigues in enumerate(({"diamond": 1, "iron": 1, "stone": 1},
                                      {"diamond": 5, "iron": 1, "stone": 1},
                                      {"diamond": 25, "iron": 5, "stone": 1})):
            if picks[i] > 0:
                temp_picks = picks.copy()
                temp_picks[i] -= 1
                result.append(
                    solve(temp_picks, minerals[5:], fatigue + sum(fatigues[mineral] for mineral in minerals[:5] ))
                )
        
        return min(result)
    
    return solve(picks, minerals, 0)



