# Last updated: 4/13/2026, 9:25:45 PM
1class Solution:
2    def buyChoco(self, prices: List[int], money: int) -> int:
3        prices.sort()
4        if prices[0]+prices[1]<=money:
5            return money-prices[0]-prices[1]
6        else:
7            return money