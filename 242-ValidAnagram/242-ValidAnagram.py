# Last updated: 3/28/2026, 12:54:51 AM
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
    
        return sorted(s)==sorted(t)
 
        