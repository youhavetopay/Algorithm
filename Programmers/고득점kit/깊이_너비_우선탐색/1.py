# 타겟 넘버

def makeSumNumber(sumValue,numbers, index, length ,targetNum, tempList):
    count = 0
    if sumValue == targetNum and index == length:
        print(index, length, sumValue, tempList, '-------------------')
        print('a')
        return 1
    else:
        if index == length and sumValue != targetNum:
            print(index, length, sumValue, tempList, 'ccccccccccc')
            print('b')
            return 0

        else:
            if index < length:
                print(index, length, sumValue, 'aaaaaaaaa', tempList)
                newList1 = tempList[:]
                newList1.append(-numbers[index])
                count += makeSumNumber(sumValue - numbers[index], numbers, index+1, length, targetNum,newList1)
                
                print(index, length, sumValue, 'b', tempList)
                newList2 = tempList[:]
                newList2.append(numbers[index])
                count += makeSumNumber(sumValue + numbers[index], numbers, index+1, length, targetNum, newList2)
                print(count, 'bbbbbbbbbb')

    return count


def solution(numbers, target):
    answer = 0

    answer = makeSumNumber(0, numbers, 0, len(numbers), target, [])

    return answer


n1 = [1, 1, 1, 1, 1]	
n2 = [2,-2,2] 
print(solution(n1, 3))
print(solution(n2, 2))