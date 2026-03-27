# Last updated: 3/28/2026, 12:54:49 AM
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        xor=0
        for i in nums:
            xor=xor^i
        for j in range(len(nums)+1):
            xor=xor^j

        return xor
        