# 중복된 원소 제거 
def removeDuplicates(self, nums) -> int:
    
    # 88ms 

    dic = {}
        
    for i in nums:
        dic[i] = 1
    
    for i, v in enumerate(list(dic.keys())):
        nums[i] = v
    
    return len(dic.keys())
    


    # 2000ms
    # index = 0
    
    # while index < len(nums):
        
    #     if nums[index] in nums[index+1:]:
    #         nums.remove(nums[index])
    #     else:
            
    #         index += 1
    
    # return len(nums)
    


    
    # 4000ms
    # index = 0
    
    # while index < len(nums):
        
    #     while nums.count(nums[index]) != 1:
    #         nums.remove(nums[index])
            
    #     index += 1
    # return len(nums)