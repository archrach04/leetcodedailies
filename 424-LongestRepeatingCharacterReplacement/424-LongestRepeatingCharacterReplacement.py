# Last updated: 8/8/2026, 11:34:38 PM
1from collections import defaultdict
2
3class Solution:
4    def characterReplacement(self, s: str, k: int) -> int:
5        left=0
6        right=0
7        freq=defaultdict(int)
8        maxx=0
9        tot=0
10
11        while right<len(s):
12            freq[s[right]]+=1
13            tot+=1
14            while (right-left+1-max(freq.values()))>k:
15                freq[s[left]]-=1
16                left+=1
17                tot-=1
18            maxx=max(maxx,tot)
19            right+=1
20        return maxx