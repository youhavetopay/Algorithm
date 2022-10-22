import heapq, sys

input = sys.stdin.readline

N = int(input())

heap = []

while N > 0:
    order = int(input())

    if order == 0:
        if heap == []:
            print(0)
        else:
            temp = heapq.heappop(heap)
            print(temp[1])
    else:
        heapq.heappush(heap, (-order, order))

    N -= 1