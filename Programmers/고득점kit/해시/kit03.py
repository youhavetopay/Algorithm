def solution(clothes):
    myCloth = {}
    count = 0
    for tempList in clothes:
        try:
            myCloth[tempList[1]].append(tempList[0])
        
        except KeyError:
            myCloth[tempList[1]] = [tempList[0]]
        
        count += 1

    coll = 1
    for value in myCloth.values():
        print(len(value))
        coll *= len(value)
    
    print(count)
    answer = count

    if coll == 1 or len(myCloth.keys()) == 1:
        return answer
    else:
        return answer+coll




list1 = [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]
list2 = [["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]]
list3 = [["crowmask", "face1"], ["bluesunglasses", "face2"], ["smoky_makeup", "face3"]]

print(solution(list3))
# list4 = [
# ["a","aa"],
# ["b","aa"],
# ["c","aa"],
# ["aa","bb"],
# ["bb","bb"],
# ["c_c","bb"],
# ["aaa","cc"],
# ["bbb","cc"],
# ["ccc","cc"]

# ]
