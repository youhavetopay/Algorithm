T = int(input())

## 문자열 중 연속적 문자 있으면 지우기 연속 2개 까지만

for test_case in range(1, T+1):
    checkStr = list(input())
    answer = 0

    flag = True

    while True:
        delLoc = -1
        flag = False
        for i in range(1, len(checkStr)):
            # 처음부터 끝까지 검사하기 만약 같은 문자가 연속적으로 있으면 처리하기
            if checkStr[i-1] == checkStr[i]:
                flag = True
                delLoc = i
                break

        # 연속적인 문자가 없을 경우 끝내기
        if flag == False:
            break
        else:
            tempList = []
            # 지울 부분은 건너 띄고 리스트에 복사
            for index, value in enumerate(checkStr):
                if index != delLoc-1 and index != delLoc:
                    tempList.append(value)

            checkStr = tempList
            
    answer = len(checkStr)

    print('#'+str(test_case), answer)