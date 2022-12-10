# Enter your code here. Read input from STDIN. Print output to STDOUT


def insert(num, heap):

    heap.append(num)
    max_length = len(heap)

    if max_length == 2: # 현재 배열의 값이 하나 밖에 없을 때
        return heap

    target_idx = max_length - 1 # 추가된 값의 위치
    parent_idx = int(target_idx / 2) # 부모의 위치

    while parent_idx != 0:

        # 부모의 값이 더 클 때
        if heap[target_idx] < heap[parent_idx]:
            heap[target_idx], heap[parent_idx] = heap[parent_idx], heap[target_idx]

            target_idx = parent_idx
            parent_idx = int(target_idx / 2)
        else:
            break
        
    return heap
    

def makeMinHeap(target_idx, heap):

    max_length = len(heap)

    child_left_idx = target_idx * 2 # 왼쪽 자식 위치
    child_right_idx = child_left_idx + 1 # 오른쪽 자식 위치

    while child_left_idx < max_length:
        if child_right_idx < max_length:

            # 현재 위치값이 자식보다 작을 때
            if heap[target_idx] <= heap[child_left_idx] and heap[target_idx] <= heap[child_right_idx]:
                return heap

            # 왼쪽 자식이 더 작을 때 
            if heap[child_left_idx] < heap[child_right_idx]:
                heap[target_idx], heap[child_left_idx] = heap[child_left_idx], heap[target_idx]
                target_idx = child_left_idx
                child_left_idx = target_idx * 2
                child_right_idx = child_left_idx + 1

            # 오른쪽 자식이 더 작을 때
            else:
                heap[target_idx], heap[child_right_idx] = heap[child_right_idx], heap[target_idx]
                target_idx = child_right_idx
                child_left_idx = target_idx * 2
                child_right_idx = child_left_idx + 1

        else: # 오른쪽 자식은 존재하지 않을 때
            if heap[target_idx] <= heap[child_left_idx]:
                return heap
            
            heap[target_idx], heap[child_left_idx] = heap[child_left_idx], heap[target_idx]
            target_idx = child_left_idx
            child_left_idx = target_idx * 2
            child_right_idx = child_left_idx + 1

    return heap

# 최소값을 삭제하는 함수
def deleteMinHeap(heap):

    heap[1], heap[-1] = heap[-1], heap[1]

    heap.pop()

    max_length = len(heap)

    if max_length <= 1:
        return heap

    heap = makeMinHeap(1, heap)

    return heap

def delete(num, heap):

    if num == heap[1]: # 삭제할려는 값이 최소값인 경우
        heap = deleteMinHeap(heap)
        return heap

    # 삭제하려는 값의 위치를 찾음
    max_length = len(heap)
    target_idx = heap.index(num)

    # 삭제하려는 값을 기준으로 가장 밑에 있는 값을 찾음
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

    # 찾은 위치를 바탕으로 최소힙 삭제를 수행
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
    