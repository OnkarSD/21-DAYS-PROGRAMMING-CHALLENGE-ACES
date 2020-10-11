#1460. Make Two Arrays Equal by Reversing Sub-arrays

#simple python solution

#1.dont need to count swaps so not many complicated calculation are required
#2.sort both the arrays if equal return True else return False

class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        
        return (sorted(target) == sorted(arr))
        
