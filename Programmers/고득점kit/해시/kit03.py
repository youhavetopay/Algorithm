def solution(clothes):
    dic1 = {}
    emptyList = []
    for tempList in clothes:
        if dic1.get(tempList[1]):
            dic1[tempList[1]].append(tempList[0])
        else:
            dic1[tempList[1]] = []
            dic1[tempList[1]].append(tempList[0])

    if len(dic1) == 1:
        return len(dic1[list(dic1.keys())[0]])

    else:
        totalValue = 0
        for i in range(0, len(list(dic1.values()))):
            totalValue += len(list(dic1.values())[i])
        tempValue = 1
        for i in range(0, len(list(dic1.values()))):
            tempValue *= len(list(dic1.values())[i]) 

        return (totalValue+tempValue)



list1 = [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]
list2 = [["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]]
list3 = [["crowmask", "face1"], ["bluesunglasses", "face2"], ["smoky_makeup", "face3"]]
list4 = [
["a","aa"],
["b","aa"],
["c","aa"],
["aa","bb"],
["bb","bb"],
["c_c","bb"],
["aaa","cc"],
["bbb","cc"],
["ccc","cc"]

]
