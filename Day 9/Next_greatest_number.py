#NEXT GREATEST NUMBER

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
    
        r = []
        for i in nums1: 
            x = nums2.index(i)
            flg = False
            for  j in range(x,len(nums2)):
                if nums2[j] > i:
                    r.append(nums2[j])
                    flg = True
                    break
            if not flg:
                r.append(-1)   
        return r
    
