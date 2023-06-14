import heapq

def solution(n, k, enemy):

    '''
        나의 풀이
        나의 병사 수, 무적권, 라운드별 병사 수가 주어질때
        몇 라운드 까지 버틸수 있는지 계산하는 문제

        나의 접근법
        약간 탐욕? 스럽게 품
        무적권을 안쓰고 넘어가는 곳은 heap에다 저장
        통과를 못하는 곳이 나오면 현재 heap에서 최대값과 비교해서
        최대값보다 작으면 heap을 pop함 (최대 값 부분에서 무적권을 쓴다고 판단)
        최대값보다 크면 무적권을 여기서 쓰는 것으로 함
        이런식으로 품

        heap pop을 하고 현재 라운드는 무적권을 안쓰고 넘어가는것이니
        현재 라운드 정보도 넣어줬어야 했는데
        그걸 모르고 한참 고민함 ㅋㅋㅋ 으이구 ㅋㅋ
    '''

    # 방어권이 라운드보다 많거나 적의 총합이 나의 병사보다 작을때는
    # 무조건 끝까지 통과할 수 있음
    if len(enemy) <= k or sum(enemy) <= n:
        return len(enemy)
    
    now_invincibility_count = k
    my_soldier = n

    heap = []

    for round in range(len(enemy)):

        # 현재 남은 병사로 해당 라운드를 넘길 수 있을 때
        if my_soldier >= enemy[round]:
            my_soldier -= enemy[round]
            heapq.heappush(heap, -enemy[round])
        else:

            # 무적권이 남아 있을 때
            if now_invincibility_count > 0:

                # heap의 최대값과 비교
                if heap and -heap[0] >= enemy[round]:
                    my_soldier += -heapq.heappop(heap) - enemy[round]
                    heapq.heappush(heap, -enemy[round])
                now_invincibility_count -= 1
                    

            else:
                # 방어권 없으면 못넘어감
                return round
            

    return len(enemy)


print(solution(7, 3, [4, 2, 4, 5, 3, 3, 1]))



def firstSolu(n, k, enemy):

    '''
        다른 사람 풀이
        프로그래머스 다른 사람 풀이
        https://school.programmers.co.kr/learn/courses/30/lessons/142085/solution_groups?language=python3


        k개 까지 전부 힙에 넣고
        넣고 빼면서 체크함 ㅋㅋㅋ
        훨씬 간단하게 풀었네 ㅋㅋㅋ

        heappushpop 이라는 것도 있네 ㅋㅋㅋㅋㅋ
    '''

    q = enemy[:k]
    heapq.heapify(q)

    for idx in range(k, len(enemy)):
        n -= heapq.heappushpop(q, enemy[idx])
        if n < 0:
            return idx
        
    return len(enemy)