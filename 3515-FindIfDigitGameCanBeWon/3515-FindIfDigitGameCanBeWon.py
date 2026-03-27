# Last updated: 3/28/2026, 12:53:48 AM
class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        small_sum = 0
        big_sum = 0

        for i in nums:
            if i < 10:
                small_sum += i
            else:
                big_sum += i

        return small_sum != big_sum