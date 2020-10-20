#CONTAINS DUPLLICATE I

#1.SET APPROCH

return len(nums) == len(set(nums))

#2.hashmap approch

dic = {}

for i in nums:
	if i in nums:
		return True
	else:
		dic[i] = 1
return True




#CONTAINS DUPLICATE II

    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
#         Time limit exceed in check
        if len(nums) == len(set(nums)):
            return False
        
        
        for i in range(len(nums)):
            for j in range(i+1,min(i+k+1,len(nums))):
                if nums[i] == nums[j]:
                    return True
        return False


