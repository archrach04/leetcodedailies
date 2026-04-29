# Last updated: 4/29/2026, 6:17:24 PM
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
13            if s[l] in vset:
14                m-=1
15            l+=1
16        
17            if s[r] in vset:
18                m+=1
19
20            r+=1
21            maxi=max(m,maxi)
22            if maxi==k:
23                return k
24        
25        return maxi
26
27
28
29
30        