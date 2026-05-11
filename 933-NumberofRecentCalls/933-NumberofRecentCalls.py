# Last updated: 5/11/2026, 9:48:10 PM
1class Solution:
2    def largestAltitude(self, gain: List[int]) -> int:
3        alt=[]
4        alt.append(0)
5        for i in range(len(gain)):
6            alt.append(alt[i]+gain[i])
7        
8        return max(alt)
9