# Last updated: 8/3/2026, 9:31:36 PM
1class Solution:
2    def longestPalindrome(self, s: str) -> str:
3        n=len(s)
4        lps=""
5
6        for i in range(n):
7
8            low=i
9            high=i
10
11            while low>=0 and high<len(s) and s[low]==s[high]:
12                low-=1
13                high+=1
14            
15            if len(s[low+1:high])>len(lps):
16                lps=s[low+1:high]
17            
18            low=i
19            high=i+1
20
21            while low>=0 and high<len(s) and s[low]==s[high]:
22                low-=1
23                high+=1
24
25            if len(s[low+1:high])>len(lps):
26                lps=s[low+1:high]
27        
28        
29        return lps
30        