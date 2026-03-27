# Last updated: 3/28/2026, 12:54:02 AM
class Solution:
    def arraySign(self, nums: List[int]) -> int:
        s=1
        for i in nums:
            s*=i
        if s>0:
            return 1
        elif s<0:
            return -1
        else:
            return 0
        