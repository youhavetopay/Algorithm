from queue import PriorityQueue # 이건 heapq보다 느림
import heapq

def solution(scoville, K):
    answer = 0
    
    queue = []

    for score in scoville:
        heapq.heappush(queue, score)
    while True:
        frist = heapq.heappop(queue)
        if frist >= K:
            return answer
        if len(queue) < 1:
            return -1
        
        second = heapq.heappop(queue)

        heapq.heappush(queue, frist+(second*2))

        answer += 1

print(solution([1,2,3], 11))