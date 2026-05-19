# Last updated: 5/20/2026, 1:56:30 AM
1class Solution:
2    def romanToInt(self, s: str) -> int:
3
4
5        dic = {
6            'I':1,
7            'V':5,
8            'X':10,
9            'L':50,
10            'C':100,
11            'D':500,
12            'M':1000
13        }
14
15        tot = 0
16        i = 0
17
18        while i < len(s):
19
20            if i < len(s)-1 and dic[s[i]] < dic[s[i+1]]:
21                tot += dic[s[i+1]] - dic[s[i]]
22                i += 2
23            else:
24                tot += dic[s[i]]
25                i += 1
26
27        return tot
28                