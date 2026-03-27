# Last updated: 3/28/2026, 12:55:06 AM
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashmp={}
        n=len(nums)
        for i in nums:
            if i in hashmp:
                hashmp[i]+=1
            else:
                hashmp[i]=1

        for j in hashmp:
            if hashmp[j]>n/2:
                return j
        

        