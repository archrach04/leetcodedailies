# Last updated: 4/15/2026, 9:31:38 PM
1class Solution:
2    def maxProfit(self, prices: List[int]) -> int:
3        prof=0
4        for i in range(1,len(prices)):
5            if prices[i]>prices[i-1]:
6                prof+=prices[i]-prices[i-1]
7        
8        return prof
9
10        