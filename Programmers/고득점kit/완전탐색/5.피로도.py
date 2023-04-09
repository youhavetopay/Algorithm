def solution(k, dungeons):

    '''
        나의 풀이
        피로도에 따라 최대 방문할 수 있는 던전의 수를 찾는 문제

        던전 개수가 최대 8이라서 DFS로 완전탐색함

        데이터크기가 컸다면 좀 많이..어려울것 같은데
        작아서 비교적 쉽게 풀었던 것 같음
    '''

    print(dungeons)

    # visit : 방문한 던전의 index
    # now_k : 남은 피로도
    def dfs(visit, now_k):
        
        # 현재 방문한 던전의 수
        answer = len(visit)

        # 던전 목록 순회
        for idx, [min_k, need_k] in enumerate(dungeons):

            # 아직 방문하지 않았고
            # 방문할 수 있는 던전인 경우
            if idx not in visit \
                and now_k >= min_k:

                # 방문 목록에 추가
                visit.add(idx)
                # 다음 던전 탐색
                answer = max(answer, dfs(visit, now_k - need_k))
                # 갔다 왔으니까 빼주기
                visit.remove(idx)

        return answer

    # DFS 시작
    answer = dfs(set(), k)
    return answer


print(solution(80, [[80,20],[50,40],[30,10]]))

import itertools

def firstSoul(k, dungeons):

    '''
        다른 사람 풀이
        https://hkim-data.tistory.com/65

        살짝 그리디..?? 한 완전탐색?? ㅋㅋ

        최대 던전 수 부터 차례대로 하나씩 내리면서 체크하는 방식
        순열을 안다면 할 수 있는 접근법인듯??
    '''
    # 최대 던전의 수
    dungeons_count = len(dungeons)

    # 던전 index 뽑기 ㅋㅋ
    dungeons_list = [i for i in range(dungeons_count)]

    # 최대 던전의 수 부터 체크 시작
    for i in range(dungeons_count, 0, -1):

        # 현재 던전의 수 만큼 순열로 뽑기
        for cases in itertools.permutations(dungeons_list, i):
            now = k
            check = True

            # 현재 순열의 던전 방문 가능성 체크
            for case in cases:
                if now < dungeons[case][0]:
                    check = False
                    break
                else:
                    now -= dungeons[case][1]
            
            if check:
                return i