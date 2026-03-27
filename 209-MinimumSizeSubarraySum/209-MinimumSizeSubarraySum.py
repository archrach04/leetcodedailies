# Last updated: 3/28/2026, 12:54:57 AM
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l,r=0,0
        mlen=float('inf')
        summ=0
        for r in range(len(nums)):
            summ+=nums[r]

            while summ>=target:
                mlen=min(mlen,r-l+1)
                summ-=nums[l]
                l+=1
        return mlen if mlen<float('inf') else 0

        