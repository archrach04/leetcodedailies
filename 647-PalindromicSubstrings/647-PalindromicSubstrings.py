# Last updated: 4/10/2026, 12:00:49 PM
1class Solution:
2    def countSubstrings(self, s: str) -> int:
3        res=0
4        for i in range(len(s)):
5            l=r=i
6            
7            while l>=0 and r<=len(s)-1:
8                if s[l]==s[r]:
9                    res+=1
10                    l-=1
11                    r+=1
12                else:
13                    break
14
15        for i in range(len(s)):
16            l=i
17            r=i+1
18            while l>=0 and r<=len(s)-1:
19                if s[l]==s[r]:
20                    res+=1
21                    l-=1
22                    r+=1
23                else:
24                    break
25
26        return res
27        