import sys
import heapq
input = sys.stdin.readline

min_heap = []
max_heap = []
check_map = {}


T = int(input())
while T > 0:

    order_count = int(input())
    while order_count > 0:

        order, n = map(str, input().split(' '))

        if order == 'I':
            heapq.heappush(max_heap, (-int(n), order_count))
            heapq.heappush(min_heap, (int(n), order_count))
            check_map[order_count] = False

        elif int(n) == 1:
            while len(max_heap) > 0 and check_map[max_heap[0][1]]:
                heapq.heappop(max_heap)

            if len(max_heap) > 0:
                pop_value = heapq.heappop(max_heap)
                check_map[pop_value[1]] = True

        else:
            while len(min_heap) > 0 and check_map[min_heap[0][1]]:
                heapq.heappop(min_heap)

            if len(min_heap) > 0:
                pop_value = heapq.heappop(min_heap)
                check_map[pop_value[1]] = True
        order_count -= 1

    while len(max_heap) > 0 and check_map[max_heap[0][1]]:
        heapq.heappop(max_heap)
    while len(min_heap) > 0 and check_map[min_heap[0][1]]:
        heapq.heappop(min_heap)
    
    if max_heap == [] or min_heap == []:
        print('EMPTY')
    else:
        print(-max_heap[0][0], min_heap[0][0])
    min_heap = []
    max_heap = []
    check_map = {}
    T -= 1