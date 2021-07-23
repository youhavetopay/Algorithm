# 해당하는 값 제거

def removeElement(self, nums, val: int) -> int:
        
    while val in nums:
        nums.remove(val)
    
    count = len(nums)
        
            
    return count