# Last updated: 3/28/2026, 12:55:46 AM
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans=[]
        n=len(nums)
        
        for i in range(n):
            if i>0 and nums[i]==nums[i-1]:
                continue
            low=i+1
            high=n-1
            while low<high:
                threesum=nums[i]+nums[low]+nums[high]
                if threesum<0:
                    low+=1
                elif threesum>0:
                    high-=1
                else:
                    ans.append([nums[i],nums[low],nums[high]])
                    low+=1
                    
                    while nums[low]==nums[low-1] and low<high:
                        low+=1


        return ans

        