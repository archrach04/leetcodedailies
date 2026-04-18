# Last updated: 4/18/2026, 5:51:55 PM
1class Solution:
2    def minWindow(self, s: str, t: str) -> str:
3        l = 0
4        shash = {}
5        thash = {}
6        word = ""
7
8        for i in t:
9            if i in thash:
10                thash[i] += 1
11            else:
12                thash[i] = 1
13
14        need = len(thash)
15        have = 0
16
17        res = float('inf')
18
19        for r in range(len(s)):
20            if s[r] in shash:
21                shash[s[r]] += 1
22            else:
23                shash[s[r]] = 1
24
25            if s[r] in thash and shash[s[r]] == thash[s[r]]:
26                have += 1
27
28            while have == need:
29                if res > (r - l + 1):
30                    res = r - l + 1
31                    word = s[l:r+1]
32
33                shash[s[l]] -= 1
34                if s[l] in thash and shash[s[l]] < thash[s[l]]:
35                    have -= 1
36
37                l += 1
38
39        return word