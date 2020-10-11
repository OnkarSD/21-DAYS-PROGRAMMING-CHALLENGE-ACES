#1614.depth of parenthesis problem

#Need to count how many open parenthesis are in equation thats the maximum depth

class Solution:
    def maxDepth(self, s: str) -> int:
        
        cdepth = 0
        fdepth = 0
        
        for c in s:
            if c == "(":
                cdepth += 1
                fdepth = max(cdepth,fdepth)
                
            if c == ")":
                cdepth -= 1
        return fdepth
