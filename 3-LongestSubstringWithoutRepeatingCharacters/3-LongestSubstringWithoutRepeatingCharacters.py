# Last updated: 3/28/2026, 12:55:55 AM
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hash_set=set()
        left=right=0
        num=0
        while right<len(s):
            while s[right] in hash_set:
                hash_set.remove(s[left])
                left+=1
            num=max(right-left+1,num)
            
            hash_set.add(s[right])
            right+=1
        
        return num
            
