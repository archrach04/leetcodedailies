# Last updated: 3/28/2026, 12:54:08 AM
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        wealth=float('-inf')
        for i in accounts:
            tot=0
            for j in i:
                tot+=j
            wealth=max(tot,wealth)
        return wealth
                
        