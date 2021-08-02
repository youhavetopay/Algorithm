list1 = [9,6,1,2,3,8,7,5,4]

def quickSort1(privot, values): # 이건 아닌듯? <-- 이거 맞음
    
    # 이론은 맞는데 append 때문에 시간복잡도 높을 듯? 
    # 코드는 간결해서 이해하기 쉬움
    # 함수 호출시 계속 리스트를 생성해서 메모리 사용측면에서 비효율적임 
    left = []
    right = []
    mid = []
    if len(values) < 2:
        return values

    # 배열의 첫번째 원소를 기준으로 작으면 왼쪽 크면 오른쪽에 추가
    for index, value in enumerate(values):
        if privot < value:
            right.append(value)
        elif privot > value:
            left.append(value)
        elif index != 0 and privot == value:
            mid.append(value)

    if left == []:
        left = []
    else:
        left = quickSort1(left[0], left)

    if right == []:
        right = []
    else:
        right = quickSort1(right[0], right)

    return left + [privot]+ mid + right


def quickSort2(values): # 제자리에서 퀵정렬하는것
    
    def sort(low, high):
        if high <= low: # 오른쪽 위치값이 왼쪽 위치값이랑 같아지면 종료 
            return 

        mid = partition(low, high)  # 가운데 값을 기준으로 위치 이동하기
        sort(low, mid-1) # 분할 (현재 privot보다 작은값들)
        sort(mid, high) # 분할 (현재 privot 보다 큰값들)

    def partition(low, high):

        privot = values[(low + high) // 2] # 기준값 가운데 있는걸루 (아무거나 상관없음)

        while low <= high: # 왼쪽 위치값이 오른쪽 위치값을 넘어갈때까지
            while values[low] < privot: # privot 보다 높은데 왼쪽에 있는거 찾기
                low += 1
            
            while values[high] > privot: # privot 보다 낮은데 오른쪽에 있는거 찾기
                high -= 1
            
            if low <= high: # 위치값들이 안 넘어 갔으면 자리 바꾸기
                values[low], values[high] = values[high], values[low]
                
                # 위치 이동
                low += 1
                high -= 1
        
        return low # 분할 기준점 반환
    

    return sort(0, len(values) - 1)
   

print(quickSort1(list1[0], list1))

list2 = [1,1,199,1,9,10]

quickSort2(list2)
print(list2)