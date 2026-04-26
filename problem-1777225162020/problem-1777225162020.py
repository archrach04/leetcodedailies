# Last updated: 4/26/2026, 11:09:22 PM
1class Solution:
2    def reverseVowels(self, s: str) -> str:
3        rev=[]
4        for i in s:
5            if i in ["a","A","i","I","E","e","o","O","U","u"]:
6                rev.append(i)
7        leng=len(rev)-1
8        for i in range(len(s)):
9            if s[i] in ["a","A","i","I","E","e","o","O","U","u"]:
10                s=s[:i]+rev[leng]+s[i+1:]
11                leng-=1
12        
13        return s
14
15