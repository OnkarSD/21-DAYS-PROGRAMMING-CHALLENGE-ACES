#211. Design Add and Search Words Data Structure

class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # self.r = defaultdict(list)
        
        self.myEx = ""
        # self.r = []
        
        

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        # self.r[len(word)].append(word)
        # print(self.r)
        
        self.myEx = self.myEx + word
        # self.r.append(word)
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        return bool(re.search(word,self.myEx))
        
#         if word in self.r:
#             return True
#         else:
#             for i in range(len(self.r)):
#                 if bool(re.search(word,self.r[i])):
#                     return True
#             return False
                
        
            
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)




#949. Largest Time for Given Digits

from itertools import permutations
class Solution:
    def largestTimeFromDigits(self, A: List[int]) -> str:
        
        
        h,m = -1,-1
        
        for t in set(permutations(A)):
            
            ch,cm = 10*t[0]+t[1],10*t[2]+t[3]
            
            if ch >= 24 or cm >= 60:
                continue
#                 invalid time
            
            if ch *60 + cm > h*60+m:
                h,m = ch,cm
            
        if (h,m) == (-1,-1):
            return ""
        else:
            clock_string = [f'{h:02}', f'{m:02}']
            return ':'.join( clock_string )
            
