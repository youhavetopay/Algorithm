# 소트인사이드

numberStr = input()

# 병합정렬로 품
def mergeSort(left, right):

    leftLen = len(left)
    rightLen = len(right)

    leftStr = left
    if leftLen > 1:
        leftStr = mergeSort(left[:leftLen//2], left[leftLen//2:])
    leftStrLen = len(leftStr)


    rightStr = right
    if rightLen > 1:
        rightStr = mergeSort(right[:rightLen//2], right[rightLen//2:])
    rightStrLen = len(rightStr)
    answer = ''

    i, j = 0, 0

    while i < leftStrLen or j < rightStrLen:
        if i >= leftStrLen and j < rightStrLen:
            answer += rightStr[j]
            j += 1
            continue
        if j >= rightStrLen and i < leftStrLen:
            answer += leftStr[i]
            i += 1
            continue

        if int(leftStr[i]) > int(rightStr[j]):
            answer += leftStr[i]
            i += 1
        else:
            answer += rightStr[j]
            j += 1

        

    return answer

print(mergeSort(numberStr[:len(numberStr)//2], numberStr[len(numberStr)//2:]))