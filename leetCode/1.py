def twoSum(nums, target):
    dic = {}
        
    for index, value in enumerate(nums):
        if target - value in dic.keys():
            dic[target - value].append(index)
            return dic[target - value]
        else:
            dic[value] = [index]
    
    
    return []

print(twoSum([2,7,11,15], 9))