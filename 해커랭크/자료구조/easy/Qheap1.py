# Enter your code here. Read input from STDIN. Print output to STDOUT


def insert(num, heap):

    heap.append(num)
    max_length = len(heap)

    if max_length == 2:
        return heap

    target_idx = max_length - 1
    parent_idx = int(target_idx / 2)

    while parent_idx != 0:
        if heap[target_idx] < heap[parent_idx]:
            heap[target_idx], heap[parent_idx] = heap[parent_idx], heap[target_idx]

            target_idx = parent_idx
            parent_idx = int(target_idx / 2)
        else:
            break
        
    return heap
    

def makeMinHeap(target_idx, heap):

    max_length = len(heap)

    child_left_idx = target_idx * 2
    child_right_idx = child_left_idx + 1

    while child_left_idx < max_length:
        if child_right_idx < max_length:

            if heap[target_idx] <= heap[child_left_idx] and heap[target_idx] <= heap[child_right_idx]:
                return heap

            
            if heap[child_left_idx] < heap[child_right_idx]:
                heap[target_idx], heap[child_left_idx] = heap[child_left_idx], heap[target_idx]
                target_idx = child_left_idx
                child_left_idx = target_idx * 2
                child_right_idx = child_left_idx + 1
            else:
                heap[target_idx], heap[child_right_idx] = heap[child_right_idx], heap[target_idx]
                target_idx = child_right_idx
                child_left_idx = target_idx * 2
                child_right_idx = child_left_idx + 1

        else:
            if heap[target_idx] <= heap[child_left_idx]:
                return heap
            
            heap[target_idx], heap[child_left_idx] = heap[child_left_idx], heap[target_idx]
            target_idx = child_left_idx
            child_left_idx = target_idx * 2
            child_right_idx = child_left_idx + 1

    return heap

def deleteMinHeap(heap):

    heap[1], heap[-1] = heap[-1], heap[1]

    heap.pop()

    max_length = len(heap)

    if max_length <= 1:
        return heap

    heap = makeMinHeap(1, heap)

    return heap

def delete(num, heap):

    if num == heap[1]:
        heap = deleteMinHeap(heap)
        return heap

    max_length = len(heap)
    target_idx = heap.index(num)

    idx_list = [target_idx]
    while len(idx_list):
        now_idx = idx_list[0]

        if now_idx * 2 < max_length:
            idx_list.append(now_idx * 2)
        else:
            break
        if now_idx * 2 + 1 < max_length:
            idx_list.append(now_idx * 2)
        else:
            break
        
        idx_list.pop(0)

    last_idx = idx_list[-1]
    heap[target_idx], heap[last_idx] = heap[last_idx], heap[target_idx]
    del heap[last_idx]
    heap = makeMinHeap(target_idx, heap)

    return heap


order_count = int(input())
heap = [None]


my_result = []


for i in range(0, order_count):
    order = input()

    if order[0] == '1':
        num = list(map(int, order.split(' ')))[1]
        heap = insert(num, heap)
    elif order[0] == '2':
        num = list(map(int, order.split(' ')))[1]
        heap = delete(num, heap)
    else:
        print(heap[1])
        my_result.append(heap[1])
    print(heap)
    