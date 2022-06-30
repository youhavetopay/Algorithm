def findSugarBagCount(weight):
    answer = 0
    while weight >= 0:

        if weight % 5 == 0:
            answer += weight // 5
            print(answer)
            return
        
        weight -= 3
        answer += 1

    print(-1)
    return

weight = int(input())

findSugarBagCount(weight)