# Last updated: 3/28/2026, 12:54:37 AM
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        S=len(s)
        T=len(t)
        j=0
        i=0
        while j<S and i<T:
            if s[j]==t[i]:
                i+=1
                j+=1
            else:
                i+=1
        
        if j==S:
            return True
        else:
            return False
