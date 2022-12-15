import heapq

def cookies(k, A):
    # Write your code here


    heapq.heapify(A)


    count = 0
    while A[0] < k:

        if len(A) < 2:
            return -1

        first = heapq.heappop(A)
        second = heapq.heappop(A)

        heapq.heappush(A, first + (2*second))
        count += 1


    return count