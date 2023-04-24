import collections
import itertools

def getFilterIds(user_ids, banned_ids):
    filtered_ids = collections.defaultdict(list)

    for ban_id in banned_ids:
        for id in user_ids:
            if len(ban_id) == len(id):

                for a, b in zip(ban_id, id):
                    if a == '*':
                        continue

                    if a != b:
                        break
                else:
                    if id not in filtered_ids[ban_id]:
                        filtered_ids[ban_id].append(id)

    return filtered_ids

def solution(user_id, banned_id):

    '''
        나의 풀이
        제재 아이디에 해당하는 아이디들의 조합을 구하는 문제

        나의 접근법
        제재된 아이디에 걸리는 아이디들을 모아두고
        중복되지 않게 조합을 하는 방식으로 함

        조합을 구하는 것 까지는 쉽게 했는데
        사용자 아이디는 중복이 없지만 제재된 아이디는 중복이 있어서
        이를 처리하는게 조금 까다로웠음..
    '''

    # 제재된 아이디의 중복 개수 체크하기
    banned_id_count = collections.Counter(banned_id)

    # 제재된 아이디별 필터링에 걸리는 아이디를 가져옴
    filtered_ids = getFilterIds(user_id, banned_id)

    # 선택한 아이디 조합들
    not_good_users = []

    # DFS로 조합 구함
    def dfs(last_banned_idx, select_ids):
        
        # 선택한 아이디들 정렬 -> 중복 체크하려고
        select_ids.sort()

        # 다 골랐고 중복이 아니라면 넣어주기
        if len(banned_id) == len(select_ids) and select_ids not in not_good_users:
            not_good_users.append(select_ids)
            return
        
        # 제재된 아이디 선택하기
        for i in range(last_banned_idx+1, len(banned_id)):

            ban_id = banned_id[i]
            count = banned_id_count[ban_id]

            # 필터링에 걸린 아이디의 조합 구하기 -> 중복된 횟수 만큼
            for now_select_ids in list(itertools.combinations(filtered_ids[banned_id[i]], count)):
                
                # 아이디의 조합들에서 이미 선택한 아이디가 없는 경우에만 다음 으로 넘어가기
                for id in now_select_ids:
                    if id in select_ids:
                        break
                else:
                    dfs(i, select_ids + list(now_select_ids))


    dfs(-1, [])

    return len(not_good_users)

print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc", "123123"], ["fr*d*", "*rodo", "******", "******"]))


from itertools import product

def check(str1, str2):
    if len(str1) != len(str2):
        return False
    
    for i in range(len(str1)):
        if str1[i] == '*':
            continue
        if str1[i] != str2[i]:
            return False
    
    return True

def firstSolu(user_id, banned_id):

    '''
        다른 사람 풀이
        프로그래머스 다른 사람 풀이

        나랑 비슷하게 품
        대신 조합이 아닌 순열로 해서 모든 경우의 수를 보고
        set으로 중복을 제거하는 방식으로 품

        훨씬 깔끔해서 보기 좋은듯??
    '''

    answer = set()
    result = [[] for i in range(len(banned_id))]

    for i in range(len(banned_id)):
        for u in user_id:
            if check(banned_id[i], u):
                result[i].append(u)
    

    result = list(product(*result))
    for r in result:
        if len(set(r)) == len(banned_id):
            answer.add("".join(sorted(set(r))))
    
    return len(answer)