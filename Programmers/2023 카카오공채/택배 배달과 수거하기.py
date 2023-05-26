def solution(cap, n, deliveries, pickups):

    '''
        나의 풀이
        배달과 수거를 모두 완료하는
        최소한의 이동거리를 구하는 문제

        나의 접근법
        그리디 하게 풀었음 ㅋㅋ
        최대한 맨 뒤에 먼저 배달하고 오면서 수거하는 방식으로 품
        근데 예외 케이스를 잘 못 찾아서 결국 질문하기를 보고 풀게 되었음
        배달 개수와 수거 개수가 없으면 리스트가 있어도 계속 돌아가기 때문에
        둘다 리스트에 전부 0인경우 0을 반환하도록 해야 함(이걸 몰라서..ㅜㅜ)


        예전에 풀었을때는 거의 다 풀었는데 마지막 케이스가 통과를 못했음..
        예전에는 pop을 안하고 계속 끝에서 부터 탐색을 해서 시간초과가 걸린듯함.. ㅋㅋㅋ
        많이 성장했다 ㅋㅋ
    '''

    answer = 0

    # 전부 0인지 체크하기
    for deliver, pick in zip(deliveries, pickups):
        if deliver != 0 or pick != 0:
            break
    else:
        # 배달할 곳과 수거할 곳이 없는 경우
        return 0

    # 모두 배달하고 모두 수거할때까지
    while deliveries or pickups:

        # 가장 멀리있는곳을 갔다가 오기
        now_move = max(len(deliveries), len(pickups))
        # 왕복 거리
        answer += (now_move * 2)

        # 배달
        now_cap = cap
        while deliveries:
            if deliveries[-1] <= now_cap:
                now_cap -= deliveries[-1]
                deliveries.pop()
            else:
                deliveries[-1] -= now_cap
                break
        
        # 수거
        now_cap = 0
        while pickups:
            if pickups[-1] + now_cap > cap:
                pickups[-1] -= cap - now_cap
                break
            else:
                now_cap += pickups.pop()

        print(deliveries, pickups)

    return answer

print(solution(2,2,[0,0],[0,0]))

def firstSolu(cap, n, deliveries, pickups):

    '''
        다른 사람 풀이
        프로그래머스 다른 사람 풀이
        https://school.programmers.co.kr/learn/courses/30/lessons/150369/solution_groups?language=python3

        나랑 비슷??? 하게 품
        근데 훨씬 효율적임

        뒤에서 부터 탐색을 하면서 이동거리를 더해줌
    '''

    answer = 0
    d = 0
    p = 0
    pos = n - 1

    for i in range(n - 1, -1, -1):
        d += deliveries[i]
        p += pickups[i]

        while d > cap or p > cap:
            d -= cap
            p -= cap

            answer += 2 * (pos + 1)
            pos = i

    if d > 0 or p > 0:
        answer += 2 * (pos + 1)

    return answer