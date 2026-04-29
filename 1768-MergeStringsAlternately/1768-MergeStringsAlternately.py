# Last updated: 4/29/2026, 6:15:24 PM
1class Solution:
2    def maxVowels(self, s: str, k: int) -> int:
3        l=0
4        r=k
5        vset={'a','e','i','o','u'}
6        maxi=0
7        m=0
8        for i in range(k):
9            if s[i] in vset:
10                m+=1
11        maxi=m
12        while r<len(s):
13            if s[r] in vset:
14                m+=1
15            if s[l] in vset:
16                m-=1
17            l+=1
18            r+=1
19            maxi=max(m,maxi)
20            if maxi==k:
21                return k
22        
23        return maxi
24
25
26
27
28        