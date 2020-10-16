#COUNT TWICE NUMBERS DICTIONARY PROBLEM

class Solution:
    def countWords(self,List, n):
        #code here
        count = 0
        dic = {}
        
        for i in List:
            
            if i in dic:
                dic[i]+=1
            else:
                dic[i] = 1
        
        for i,v in dic.items():
            if v == 2:
                count += 1
        
        return count
