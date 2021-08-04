# 힙정렬

arr = [
    None, 
    1, 3, 5,
    7, 9, 11,
    13, 15, 14,
    12, 10, 8,
    6, 4, 2
]

arrLength = len(arr)-1

def makeMaxHeep(index):
    
    global arr, arrLength

    # 자식노드가 없을때
    if index*2 > arrLength:
        return

    # 자식노드가 양쪽다 있을 때
    if index*2+1 <= arrLength:

        # 만약 자식 노드 중 자기보다 높은 값 있는지 검사
        if arr[index] < arr[index*2] or arr[index] < arr[index*2+1]:
            
            # 왼쪽이 높은지 오른쪽이 높은지 찾고 해당 값이랑 바꾸기
            if arr[index*2] > arr[index*2+1]:
                arr[index], arr[index*2] = arr[index*2], arr[index]

            else:
                arr[index], arr[index*2+1] = arr[index*2+1], arr[index]

            # 바꾸는 과정에서 이전에 했던 구조가 망가졌을까봐 처음부터 다시 검사
            makeMaxHeep(1)
        
        else:
            # 현재 노드 값이 최대힙 구조를 만족하면 다음 노드로 이동
            makeMaxHeep(index+1)
    
    else: # 자식노드가 왼쪽만 있을 때
        if arr[index] < arr[index*2]:
            arr[index], arr[index*2] = arr[index*2], arr[index]

            makeMaxHeep(1)
        else:
            makeMaxHeep(index+1)

def heepSort():

    global arr, arrLength

    if arrLength < 2:  # 힙정렬 종료 조건
        return
    
    # 최대값과 가장 끝 노드의 값 바꾸기
    arr[1], arr[arrLength] = arr[arrLength], arr[1]

    # 최대 값이 제일 뒤로 갔으니(정렬) 뒤에꺼는 안건들이기
    arrLength -= 1

    # 최대 힙이 망가졌으니 다시 만듬
    makeMaxHeep(1)

    # 반복
    heepSort()


makeMaxHeep(1)

print(arr)

heepSort()

print(arr)
