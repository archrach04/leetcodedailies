# Last updated: 8/4/2026, 10:45:01 PM
1class Solution:
2    def lengthOfLongestSubstring(self, s: str) -> int:
3        hashs=set()
4        l=0
5        r=0
6        maxl=0
7        while r<len(s):
8            if s[r] not in hashs:
9                hashs.add(s[r])
10                maxl=max(maxl, len(s[l:r+1]))
11                r+=1
12            else:
13                while s[r] in hashs:
14                    hashs.remove(s[l])
15                    l+=1
16        
17        return maxl
18            
19