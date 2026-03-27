# Last updated: 3/28/2026, 12:54:25 AM
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack=[]
        res=[0]*len(temperatures)
        for i in range(len(temperatures)):
            while stack and temperatures[i]>stack[-1][0]:
                num,ind=stack.pop()
                res[ind]=i-ind
            stack.append((temperatures[i],i))
        
        return res
           
                
                