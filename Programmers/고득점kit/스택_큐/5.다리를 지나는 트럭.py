import collections

def solution(bridge_length, weight, truck_weights):

    '''
        나의 풀이
        모든 트럭이 다리를 지나가는 걸리는 시간을 구하는 문제

        큐 두개 사용해서 품
        예전에 풀었던 기억이 있는거 같은데
        확실하게는 모르겠음 ㅋㅋ

        한턴씩 직접 전부 그대로 구현하기 때문에
        조금은 비효율적일 수도 있지만
        그래도 10,000까지는 아주 넉넉하게 버티는 듯.. ㅋㅋ
    '''

    answer = 0

    # 아직 건너지 못한 트럭의 대기 큐
    wait_queue = collections.deque(truck_weights)

    # 현재 다리를 지나가고 있는 트럭 큐
    cross_queue = collections.deque()
    # 현재 다리위에 올라와 있는 총 무게
    now_cross_weight = 0

    # 두개의 큐를 모두 비울때까지 -> 모두 다리를 건널때 까지
    while wait_queue or cross_queue:
        
        # 현재 다리 위에 있는 트럭 이동시키기
        for i in range(len(cross_queue)):
            cross_queue[i][1] -= 1

        # 현재 다리 위에 있는 맨 앞에 있는 트럭이 다리 끝에 도착했을 때
        # 동시에 도착하는 트럭은 없음 -> 맨앞에가 도착하면 한턴 뒤에 다른 트럭이 도착할 수 있음
        # -> 한번에 한대씩만 도착
        if cross_queue and cross_queue[0][1] == 0:
            finish_weight, _ = cross_queue.popleft()
            now_cross_weight -= finish_weight

        # 아직 다리를 지나지 못한 트럭이 있고
        # 해당 트럭이 다리에 들어와도 다리는 무게를 버틸 수 있고
        # 다리에 해당 트럭이 들어올 자리가 있을 때
        # 트럭은 다리를 건너기 시작함
        if wait_queue and now_cross_weight + wait_queue[0] <= weight and len(cross_queue) < bridge_length:
            now_weight = wait_queue.popleft()
            cross_queue.append([now_weight, bridge_length])
            now_cross_weight += now_weight
        
        # 걸리는 시간 플러스 해주기
        answer += 1
        


        print(wait_queue)
        print(cross_queue)

    return answer

print(solution(2, 10, [7,4,5,6]))

def firstSoul(bridge_length, weight, truck_weights):
    
    '''
        다른 사람 풀이
        https://jminie.tistory.com/157

        나랑 얼추 비슷하지만
        
        다리를 건너고 있는 큐에 빈공간에 0을 넣어줌으로써
        굳이 다리를 건너고 있는 로직 (길이에서 -1 해주는 for문)을 뺴고
        길이 체크 등등 여러 로직이 빠져서

        시간 복잡도도 좀더 좋고
        훨씬 깔끔한 코드인듯 함
        
    '''

    answer = 0
    temp = 0
    truck_bridge_deque = collections.deque(bridge_length * [0])
    truck_weights_deque = collections.deque(truck_weights)

    while len(truck_bridge_deque):

        answer += 1
        temp -= truck_bridge_deque[0]
        truck_bridge_deque.popleft()

        if truck_weights_deque:
            if temp + truck_weights_deque[0] <= weight:
                temp += truck_weights_deque[0]
                truck_bridge_deque.append(truck_weights_deque.popleft())
            else:
                truck_bridge_deque.append(0)

    return answer