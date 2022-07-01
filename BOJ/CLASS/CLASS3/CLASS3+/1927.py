import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

N = int(input())
heap_queue = [None]
heap_length = 1

def addHeap(x):
    global heap_queue, heap_length

    heap_queue.append(x)
    idx = heap_length - 1

    p_idx = idx // 2
    while p_idx != 0:
        print(p_idx, idx)
        if heap_queue[idx] < heap_queue[p_idx]:
            heap_queue[idx], heap_queue[p_idx] = heap_queue[p_idx], heap_queue[idx]
            idx = p_idx
        p_idx = p_idx // 2

    return




while N > 0:

    x = int(input())

    if x != 0:
        heap_length += 1
        addHeap(x)
    else:
        pass
    print(heap_queue, heap_length)
    N -= 1