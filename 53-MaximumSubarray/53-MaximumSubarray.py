# Last updated: 3/28/2026, 12:55:34 AM
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        subarray_sum=0
        maxsum=nums[0]

        for cursum in nums:
            if subarray_sum<0:
                subarray_sum=0
            subarray_sum+=cursum
            maxsum=max(maxsum,subarray_sum)
        return maxsum
        