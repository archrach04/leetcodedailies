# Last updated: 8/4/2026, 1:11:22 PM
1class Solution:
2    def reverseWords(self, s: str) -> str:
3        
4        char=s.split()
5        res=""
6        for i in range(len(char)-1,-1,-1):
7            if i==0:
8                res+=char[i]
9            else:
10                res+=char[i]+" "
11        return res
12
13
14                
15        