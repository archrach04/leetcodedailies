# Last updated: 4/27/2026, 10:44:28 PM
1class Solution:
2    def mergeAlternately(self, word1: str, word2: str) -> str:
3        res=""
4        if len(word1)>len(word2):
5            for i in range(len(word2)):
6                res+=word1[i]+word2[i]
7            res+=word1[len(word2):]
8            return res
9
10        elif len(word1)<len(word2):
11            for i in range(len(word1)):
12                res+=word1[i]+word2[i]
13            res+=word2[len(word1):]
14            return res
15
16
17        else:
18            for i in range(len(word1)):
19                res+=word1[i]+word2[i]
20            return res
21
22        