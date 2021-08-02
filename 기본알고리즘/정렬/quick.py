list1 = [9,6,1,2,3,8,7,5,4]

def quickSort1(privot, values): # 이건 아닌듯?
    
    # 이론은 맞는데 append 때문에 시간복잡도 높을 듯?
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


def quickSort2(privot, values):
    leftLoc = 1
    rightLoc = len(values) - 1


   

print(quickSort1(list1[0], list1))