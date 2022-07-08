def solution(clothes):
    myCloth = {}
    answer = 0
    for tempList in clothes:
        try:
            myCloth[tempList[1]] += 1
        
        except KeyError:
            myCloth[tempList[1]] = 1

    coll = 1
    for key, value in myCloth.items():
        coll *= value + 1
    
   
    answer = coll - 1
    return answer




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
