# Last updated: 3/28/2026, 12:55:45 AM
class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        ch={'(':')', '{':'}', '[':']'}
        for i in s:
            if i in ch:
                stack.append(ch[i])
            elif len(stack)!=0 and i==stack[-1]:
                stack.pop()
            else:
                return False

        return True if len(stack)==0 else False
            

                

        