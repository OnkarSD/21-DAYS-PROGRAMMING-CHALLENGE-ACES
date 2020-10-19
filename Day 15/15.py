#SUM OF ODD LENGTH SUBARRAYS

class Solution:
    def sumOddLengthSubarrays(self, A: List[int]) -> int:
        n = len(A)
        s = 0
        
        for l in range(1,n+1,2):
            for i in range(n-l+1):
                s = s + sum(A[i:i+l])
        return s


#LONGEST COMMON PREFIX ARRAY

for _ in range(int(input())):
    n = int(input())
    strs = [x for x in input().split()]
    
    s = ""
    if len(strs)==0: #edge case, no elements in list
        print(s)
    elif len(strs)==1: #edge case, single element in list
        print(strs[0])

    #word length of shortest word to prevent index out of range
    for a in range(len(min(strs))): 
        #loops through each word in list, starting with second word
        for b in range(1, len(strs)): 
            #compares nth character of first word to other words
            if strs[0][a]==strs[b][a]: 
                #only adds to pattern if nth character same up to the last word
                if b==len(strs)-1: 
                    s += strs[0][a]
            else: #exits when characters don't match
                break
    print(s)
        
        
