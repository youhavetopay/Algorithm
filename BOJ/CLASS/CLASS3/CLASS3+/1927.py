import sys
import heapq
input = sys.stdin.readline

N = int(input())
heap_length = 1

heap = []

while N > 0:

    order = int(input())

    if order == 0:
        if heap == []:
            print(0)
        else:
            print(heapq.heappop(heap))
    else:
        heapq.heappush(heap, order)

    N -= 1