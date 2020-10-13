#Daily Temprature 



class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        
        r = [0]*len(temp)
        stack =[]
        
        for i,t in enumerate(temp):
            
            while stack and stack[-1][1] < t:
                index,value = stack.pop()
                r[index] = i-index
                
            
            stack.append([i,t])
            
        return r
                

#brootforce doesnt work TLE
        
#         r = [0]*len(T)
        
#         for i in range(len(T)):
#             for j in range(i,len(T)):
                
#                 if T[j] > T[i]:
#                     r[i] = j-i
#                     break
#         return r




        
        
