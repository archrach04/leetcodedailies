# Last updated: 3/28/2026, 12:54:39 AM
class Solution:
    def firstUniqChar(self, s: str) -> int:
        hashs={}
        for i in s:
            if i in hashs:
                hashs[i]+=1
            else:
                hashs[i]=1
        i=0
        for ch in s:
            if hashs[ch]==1:
                return i
            i+=1
        return -1