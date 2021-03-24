def solution(clothes):
    answer = 0
    return answer



list1 = [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]
list2 = [["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]]
dic1 = {}
emptyList = []
for tempList in list1:
    if dic1.get(tempList[1]):
        dic1[tempList[1]].append(tempList[0])
    else:
        dic1[tempList[1]] = []
        dic1[tempList[1]].append(tempList[0])
        

# for key, value in dic1.items():
#     if ' ' in value:
#         dic1[key] = list(value.split(' '))



