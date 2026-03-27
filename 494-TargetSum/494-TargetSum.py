# Last updated: 3/28/2026, 12:54:36 AM
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total = sum(nums)

        # If transformation not possible
        if (target + total) % 2 != 0 or abs(target) > total:
            return 0

        subset_sum = (target + total) // 2

        dp = [0] * (subset_sum + 1)
        dp[0] = 1

        for num in nums:
            for s in range(subset_sum, num - 1, -1):
                dp[s] += dp[s - num]

        return dp[subset_sum]